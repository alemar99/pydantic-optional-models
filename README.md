# Auto-generated pydantic models with optional fields

The idea is to have the script `generate_partial_models.py` to automatically manage the generation of models with all the fields being optional.

The original models are under `src/models/` while the generated ones are under `src/partialmodels`.

To generate a partial model just add the `generate_partial()` decorator to the model.

Then run:
```
./generate_partial_models.py
```

## Key Features
- Supports both **Pydantic v1** and **Pydantic v2**
- **Automatically generates** partial models from existing ones
- **Detects changes** in model name, field names, or types to determine whether regeneration is needed (run with `--check`)
- Use a simple `@generate_partial` decorator to flag models for generation
- Add **custom methods** to the generated models without worrying about overwrites
- Includes a base class for partial models where you can define shared logic or behavior (see the `safe_get` method)

