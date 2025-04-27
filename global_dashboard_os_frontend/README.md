global_dashboard_os_frontend

UI app module setup:

* Create folder called `templates`: holds html templates.
* Create folder called `static`: holds all static files.
  * Create sub folder called `frontend`: holds javascript bundle, which comes from react source code.
  * Create sub folder called `css`: holds CSS files.
  * Create sub folder called  `images`: holds image files.
* Create a folder called `src`: holds react source code
  * Create a sub folder called `components`: holds react components

* Run below command, from `global_dashboard_os_frontend`, to initialize: create node module, create package.json, etc.
  * `npm init -y`
* Run below commands, from `global_dashboard_os_frontend`, to install various packages / components required for a react web app:
  * `npm i webpack webpack-cli --save-dev` : bundle javascript and transpile??? After executing this command,
    we will see `package-lock.json` file and `node_modules` folder. It is interesting to check the content of these two items.
  * `npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev`  : takes our code and makes it compatible with various browsers, including older browsers???
  * `npm i react react-dom --save-dev` : install react and react dom
  * `npm install @material-ui/core`: style webpage, it has things like bootstrap???; I had to use `npm install @material-ui/core --force` and I also tried `npm install @material-ui/core --legacy-peer-deps`
  * `npm install @babel/plugin-proposal-class-properties`: we can use async and wait; I had to use `--force` and also tried `--legacy-peer-deps`
  * `npm install react-router-dom`: enables us to re-route pages; I had to use `--force`
  * `npm install @material-ui/icons`: for icons
* Create `babel.config.json` in `global_dashboard_os_frontend` and populate as shown in this github file. This allows us to use some preset entries and async and wait related properties???
* Create `webpack.config.js` in `global_dashboard_os_frontend` and populate. Webpack bundles all js in one file, serves that one file to browser.
* Add this entry to `package.json`'s `scripts`: `"dev" : "webpack --mode development --watch"`. This will enable us to see js changes during development, we run this in watch mode, i. e., watch for changes???
* Add another entry to `package.json`'s `scripts` : `"build" : "webpack --mode production"` 
* Next, inside `src` folder create `index.js` file and populate as in this github source.
* Note: for our react+django combination, django renders pages but react takes over for dynamic contents of the pages. Next, we need to create files and contents accordingly for our minimum frontend implementation.
* Create sub folder `frontend` inside folder `templates`
* Inside `/templates/frontend`, create a file `index.html` and populate. Note `id="app"` in nested `<div>` tag, this is the id that is used to link.
* Inside `/static/css`, create a file `index.css` and populate.
* Next, edit `views.py` for rendering.
* Create `urls.py` and create mapping as shown, i.e., when user enters base url, link it to `index` function of `views.py`, which in turn redirects that to `frontend/index.html`. 
* Create a link in `globas_dashboard_os/urls.py`: `path('', include('global_dashboard_os_frontend.urls'))`
* Create `App.js` in `src/components` folder and populate.
* Create `index.js` in `src` folder and link `./components/App`
* Add linking information in `settings.py` in the main project: `'global_dashboard_os_frontend.apps.GlobalDashboardOsFrontendConfig'`.

Running frontend server:
-----------------------
* `npm run dev` : here `dev` refers to `dev` `"dev" : "webpack --mode development --watch",` in `package.json`.
  Now, if we check `/static/frontend` folder, we should see main.js, which is bundled javascript code that was generated.
  Note: If we need to build production version  run command `npm run build`.
  