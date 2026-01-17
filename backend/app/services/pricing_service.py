from typing import List, Dict, Any
from app.services.product_service import product_service

class PricingService:
    MARGIN_MULTIPLIER = 1.7

    def calculate_price(self, product: Dict) -> float:
        """
        Calculate final price.
        Internal products: List price.
        External products: Price * 1.7 margin.
        """
        price = product.get('price', 0)
        if str(product.get('id', '')).startswith('EXT'):
            return int(price * self.MARGIN_MULTIPLIER)
        return int(price)

    def create_bundle(self, budget: int) -> Dict[str, Any]:
        """
        Smart Product Bundling Logic.
        Try to find a combination of item A + B + C <= budget.
        Using a simple greedy approach with randomization for variety.
        """
        all_products = product_service.get_all_products()
        import random
        # Shuffle to get different results
        candidates = all_products.copy()
        random.shuffle(candidates)

        bundle_items = []
        current_total = 0

        # Attempt to fill budget with different categories if possible
        categories_found = set()

        for product in candidates:
            final_price = self.calculate_price(product)
            
            if current_total + final_price <= budget:
                # Add to bundle
                bundle_items.append({
                    **product,
                    "final_price": final_price,
                    "original_price": product["price"] # Keep track of original
                })
                current_total += final_price
                categories_found.add(product.get('category', 'General'))
            
            # Stop if we are close enough (e.g., within 5% or simply full)
            if current_total >= budget * 0.95:
                break

        return {
            "budget": budget,
            "total_price": current_total,
            "items": bundle_items,
            "remaining_budget": budget - current_total
        }

pricing_service = PricingService()
