import json
import os
from typing import List, Dict, Optional

class ProductService:
    def __init__(self):
        self.internal_products = []
        self.external_products = []
        self._load_data()

    def _load_data(self):
        # Load Internal Data
        try:
            with open("app/data/internal_products.json", "r") as f:
                self.internal_products = json.load(f)
        except FileNotFoundError:
            print("Internal products file not found.")
            self.internal_products = []

        # Load External Data
        try:
            with open("app/data/external_products.json", "r") as f:
                self.external_products = json.load(f)
        except FileNotFoundError:
            print("External products file not found.")
            self.external_products = []

    def get_all_products(self) -> List[Dict]:
        return self.internal_products + self.external_products

    def search_products(self, query: str) -> List[Dict]:
        query = query.lower()
        results = []
        
        # Simple search implementation
        for product in self.get_all_products():
            if query in product['name'].lower() or \
               query in product.get('category', '').lower():
                results.append(product)
        
        return results

    def get_product_by_id(self, product_id: str) -> Optional[Dict]:
        for product in self.get_all_products():
            if product['id'] == product_id:
                return product
        return None

product_service = ProductService()
