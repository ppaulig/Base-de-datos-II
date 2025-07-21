from bson import ObjectId

def convertir_ids(obj):
    if isinstance(obj, list):
        return [convertir_ids(o) for o in obj]
    elif isinstance(obj, dict):
        return {
            k: str(v) if isinstance(v, ObjectId) else convertir_ids(v)
            for k, v in obj.items()
        }
    else:
        return obj