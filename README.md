Lute language definitions.

This directory of languages is added as a git submodule to lute itself.

# Adding a language

## Manual method

For each new language:

1. create a directory with the name of the language (really it can be anything)
2. create `definition.yaml` from `_templates/definition.yaml.example`, fill it in.  The file name **matters**.
3. create a story .txt file from `_templates/story.yaml.example`, fill it in.  The file name **does not matter**.

## Scripted

You can export a language and the first few pages of its book in Lute itself, assuming that you have loaded the language in your db:

```
python -m scripts.dump_lang_data Afrikaans Dutch
```

These are exported to `lute/db/language_defs`.  The file changes can be committed in that submodule repository, and PRs opened to the language-defs repository as usual.

# Verifying

To verify the files, run

```
python verify_files.py
```

This does a simple sanity check of the files, it's not an exhaustive check.

The file definitions are also checked during Lute's CI.

# Including the latest languages in lute-v3 itself

This project is included as a git submodule in Lute, so if this repo's `master` branch changes, just update the reference:

```
# in root directory of lute itself
pushd lute/db/language_defs
git checkout master
git fetch origin
git merge origin/master  # could also do git pull
popd
git add lute/db/language_defs
git commit -m "Update language defs."
```

# Notes

## Why is this a git submodule?

This directory/repo is just data, so ideally it would be pulled in at build time, but I had problems including the data files when packaging with flit.  Submodules was the easiest solution I could come up with at the time.  There is probably an easier way to do it, but this way works fine for now.
