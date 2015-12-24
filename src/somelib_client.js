var request = require('request');

var clientApi = {
    host : 'http://0.0.0.0:8080',
    g : function(action, args){
        if(arguments.length < 2) {
            return {};
        } else {
            var options = {
                'url': this.host,
                'method': 'GET'
            };
            var callback = arguments[arguments.length - 1];
            for(var i = 0; i < arguments.length - 1; i++) {
                options['url'] += '/' + arguments[i];
            }
            request(options, function(err, res, body) {
                callback(err, res, body);
            });
        }
    },
    mouse: function(cheese, trap, cat, cb){
        this.g('mouse', cheese, trap, cat, cb);
    },
    dog: function(bone, cb){
        this.g('dog', bone, cb);
    }
};
