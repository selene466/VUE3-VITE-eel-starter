# Vue starter project for Eel

This is a starter template [eel](https://github.com/python-eel/Eel) + [VUE.js 3](https://vuejs.org/) + [VITE](https://vitejs.dev/). It will create a local app with python as backend and VITE + VUE3 as front-end.
It is not unlike electron...

## Whats new

- Added Tailwind v3
- Integrated UI with daisyUI v4
- Automatic class sorting with Prettier
- Auto import components & layouts
- Auto import icons
- Auto router
- Support for theme changer
- Installed iconify-json to work offline: bxs, fluent, ic, mdi, noto
- Use webview instead of Chrome engine

Check `vite.config.js.

## Start a new app

Copy this repo and you are ready to start.

### Installation

```cmd
pip install eel
pip install webview
cd web-src
yarn
```

### Develop front-end

Run the VUE app.

```cmd
cd web-src
yarn dev
```

With in `web-src\public\eel.js` there is a mock-up eel implementation. This file will be overwritten when building.
It holds 2 example functions `hello_world` and `get_greeting`.
`get_greeting` has also the callback logic.
These are just for testing so you can quickly develop the front-end like you would with every VUE app.

### Build front-end

Running the build command will create a folder `/web`. This folder holds build VUE app.

```cmd
cd web-src
yarn build
```

### Develop eel.js

Eel can now be build in the same way as normal.

```cmd
python app.py
```

All the mock-up function with `eel.js` are now overwritten by the eel app.
If the eel exposed function in `app.py` are called the same it will work directly.

### Building the full app

This will build the front-end and then the app as one `.exe` file.

```cmd
cd web-src
yarn build
cd ..
pip install pyinstaller
python -m eel app.py web --onefile
```

### Manual build with `pyinstaller`.

Follow the instructions below.

```cmd
cd web-src
yarn build
cd ..
pip install pyinstaller
```

Build normally with support for printing in the console.

```cmd
pyinstaller --noconfirm --hide-console hide-early --clean --add-data "web/:web/" --name "YourAppName" "app.py"
```

Build compressed one file without support for printing in the console, which may take time to decompress.

```cmd
pyinstaller --noconfirm --noconsole --onefile --clean --add-data "web/:web/" --name "YourAppName" "app.py"
```

Build compressed one file with support for printing in the console but then hide the console to avoid `sys.std*` error.

```cmd
pyinstaller --noconfirm --hide-console hide-early --onefile --clean --add-data "web/:web/" --name "YourAppName" "app.py"
```

## Update your current project

Within `index.html` add:

```html
<script type="text/javascript" src="/eel.js"></script>
```

In `vite.config.js` add a `build - outDir`

```js
export default defineConfig({
  ...
  plugins: [vue()],
  build: {
    outDir: "../web",
  },
  ...
});
```

### eel.js debugger [Optional]

Copy the `public/eel.js` into your public folder.
This script creates a mockup eel so you can test your VUE app without building or running the eel app.
