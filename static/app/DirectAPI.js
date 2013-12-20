Ext.define('MyApp.DirectAPI', {
    requires: ['Ext.direct.*']
}, function() {
    var Loader = Ext.Loader,
        wasLoading = Loader.isLoading;
    Loader.loadScriptFile('http://127.0.0.1:5000/direct/api', Ext.emptyFn, Ext.emptyFn, null, true);
    Loader.isLoading = wasLoading;
    Ext.direct.Manager.addProvider(Ext.app.REMOTING_API);
});