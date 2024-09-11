schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "primary": {"type": "boolean"},
        "ingredients": {
            "type": "array",
            "items": {"$ref": "#/$defs/item_amount"},
        },
        "products": {
            "type": "array",
            "items": {"$ref": "#/$defs/item_amount"},
        },
        "duration": {"type": "integer", "minimum": 0.001}
    },
    "required": ["name", "primary", "ingredients", "products", "duration"],
    
    "$defs": {
        "item_amount": {
            "type": "object",
            "properties": {
                "item": {"type": "string"},
                "amount": {"type": "integer", "minimum": 1}
            },
            "required": ["item", "amount"]
        }
    }
    
}