from typing import List, Dict, Any
import re
from app.services.pricing_service import pricing_service
from app.services.product_service import product_service

class ChatService:
    def process_message(self, message: str) -> Dict[str, Any]:
        """
        Process user message and return a response.
        Currently uses regex to detect intent (Budget or Search).
        Future: Integrate Gemini API here.
        """
        message_lower = message.lower()

        # 1. Budget / Bundling Intent
        # Look for numbers like "200rb", "200.000", "200000"
        budget_match = re.search(r'(\d+)(?:rb|k|\.000|000|\d{3})', message_lower)
        
        # Relaxed intent keywords: budget, seharga, uang, rp (if followed by number)
        is_budget_intent = any(kw in message_lower for kw in ["budget", "seharga", "uang", "dana"])
        if (is_budget_intent or "rp" in message_lower) and budget_match:
            try:
                raw_match = budget_match.group(0)
                amount_prefix = int(budget_match.group(1))
                amount = amount_prefix

                # Fix Parsing Logic
                if 'rb' in raw_match or 'k' in raw_match:
                    amount *= 1000
                elif raw_match.endswith('.000') or raw_match.endswith('000'):
                    # User likely typed 200.000 or 200000. group(1) caught 200.
                    # We must assume the suffix meant thousands if the prefix is small
                    # OR simply treat it as the full number if we parsed it via regex (which splits it).
                    # Actually, if regex is (\d+)(...000), group(1) might be 200.
                    # Safety check: if amount is small (<1000) and we see '000', multiply.
                    if amount < 1000: 
                        amount *= 1000
                elif len(str(amount)) < 4: 
                    # E.g. "200" without suffix, but context implies budget -> assume 'k'
                    amount *= 1000

                # Generate Bundle
                bundle = pricing_service.create_bundle(amount)
                
                # Format Response
                response_text = f"Oke, dengan budget Rp {amount:,}, saya sarankan kombinasi berikut:\n\n"
                for item in bundle['items']:
                    response_text += f"- {item['name']} (Rp {item['final_price']:,})\n"
                
                response_text += f"\nTotal: Rp {bundle['total_price']:,}. Sisa Budget: Rp {bundle['remaining_budget']:,}."
                
                return {
                    "response": response_text,
                    "data": bundle,
                    "type": "bundle"
                }
            except Exception as e:
                return {"response": f"Maaf, saya salah hitung: {str(e)}", "type": "error"}

        # 2. Search Intent
        if "cari" in message_lower or "ada" in message_lower:
            # Extract query (very naive)
            query = message.replace("cari", "").replace("apakah ada", "").replace("ada", "").strip()
            if query:
                results = product_service.search_products(query)
                if results:
                    response_text = f"Saya menemukan {len(results)} produk untuk '{query}':\n"
                    # Limit to 5
                    for item in results[:5]:
                        price = pricing_service.calculate_price(item)
                        response_text += f"- {item['name']} - Rp {price:,}\n"
                    return {"response": response_text, "data": results, "type": "search"}
                else:
                    return {"response": f"Maaf, tidak ada produk '{query}' yang ditemukan.", "type": "search_empty"}

        # 3. Default / Greeting
        return {
            "response": "Halo! Saya asisten AI Anda. Anda bisa tanya stok produk atau minta rekomendasi bundling sesuai budget (misal: 'Saya punya budget 200rb').",
            "type": "text"
        }

chat_service = ChatService()
