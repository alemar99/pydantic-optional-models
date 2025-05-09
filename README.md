# Auto-generated pydantic models with optional fields

The idea is to have the script `generate_partial_models.py` to automatically manage the generation of models with all the fields being optional.

The original models are under `src/models/` while the generated ones are under `src/partialmodels`.

To generate a partial model just add the `generate_partial()` decorator to the model.

Then run:
```
./generate_partial_models.py
```

You can also pass the `--check` flag to check if it's needed to execute the script again (useful in the CI for example)


Supports both Pydantic v1 and Pydantic v2.
