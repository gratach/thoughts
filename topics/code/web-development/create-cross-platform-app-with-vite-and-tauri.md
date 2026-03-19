# Create cross-platform app with vite and tauri

## Create the app

Following the instructions of ChatGPT the app can be created in the following way:

```
npm create vite@latest test-tauri -- --template react-ts
cd test-tauri
npm install
npm install -D @tauri-apps/cli
npx tauri init
```

On Debian 12 the following additional steps where necessary to run the app.
- **installation of the latest node version**
	See: [nodejs download](https://nodejs.org/en/download)
- **installation of the latest cargo version**
	See: [rust installation](https://rust-lang.org/tools/install/)
- **installation of `libgtk-3`**
	`apt install libgtk-3-dev`
- **installation of `libwebkit2gtk-4.1`**
	`apt install libwebkit2gtk-4.1-dev

In `package.json` the following line should be inseted in the `"scripts": { ... }` paragraph:
`"tauri": "tauri"`

## Run and build the app

Build the web app into the dist folder:
`npm run build`

Serve the app editable in dev mode:
`npm run dev`
Press o to open in browser.

Serve the app as desktop application editable in dev mode:
`npm run tauri dev`