module.exports = function(config){
  var opalPath = process.env.OPAL_LOCATION;
  var karmaDefaults = require(opalPath + '/opal/tests/js_config/karma_defaults.js');
  var baseDir = __dirname + '/..';
  var coverageFiles = [
    __dirname +  '/../dischargesummary/static/js/dischargesummary/controllers/*.js',
  ];
  var includedFiles = [
    __dirname +  '/../dischargesummary/static/js/dischargesummary/controllers/*.js',
    __dirname + '/../dischargesummary/static/js/test/*.js',
  ];

  var defaultConfig = karmaDefaults(includedFiles, baseDir, coverageFiles);
  config.set(defaultConfig);
};
