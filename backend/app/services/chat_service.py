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
        budget_match = re.search(r'(\d+)(?:rb|k|\.000|000)', message_lower)
        if "budget" in message_lower and budget_match:
            try:
                # Extract amount. If 'rb' or 'k', multiply by 1000.
                amount_str = budget_match.group(1).replace('.', '')
                amount = int(amount_str)
                if 'rb' in budget_match.group(0) or 'k' in budget_match.group(0):
                    amount *= 1000
                elif budget_match.group(0).endswith('.000'):
                     pass # Already full number
                elif len(amount_str) < 4: # e.g. "200" interpreted as 200k if simplistic
                     amount *= 1000 # Safe assumption for "200 budget"

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
