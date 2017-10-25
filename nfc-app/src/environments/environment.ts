// The file contents for the current environment will overwrite these during build.
// The build system defaults to the dev environment which uses `environment.ts`, but if you do
// `ng build --env=prod` then `environment.prod.ts` will be used instead.
// The list of which env maps to which file can be found in `.angular-cli.json`.

export const environment = {
  production: false,
  firebase: {
    apiKey: "AIzaSyCP1HtrbReWHgOFQDMv3B8_WVyOCc18UJg",
    authDomain: "nmd-cms.firebaseapp.com",
    databaseURL: "https://nmd-cms.firebaseio.com",
    projectId: "nmd-cms",
    storageBucket: "nmd-cms.appspot.com",
    messagingSenderId: "84102007611"
  }
};
