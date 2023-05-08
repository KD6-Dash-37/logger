# Logger

To add this repo as a submodule of another repo:

```
git submodule add https://github.com/KD6-Dash-37/logger <path/to/logger/directory>
```

To update the submodule:

```
git submodule update --remote <path/to/logger/directory>
```

When you clone and the repo and want to include the submodule:

```
git clone --recursive <repository-url>
```

If you have already cloned the repo and the submodule was not included:

```
git submodule update --init --recursive
```
