odoo.define('collages_mis.ClientAction', function (require) {
"use strict";

var core = require('web.core');
var AbstractAction = require('web.AbstractAction');
var Widget = require('web.Widget');
var collageTemplate = AbstractAction.extend({
    template: "collage_template",

    events: {
        'click .add' : 'addnew'
    },

     start: function(){
       this._super.apply(this, arguments);
       this.addnew()

    },

    addnew : function (){
        var counter = new Counter(this,0);
        counter.appendTo('.container');

    }

});

var Counter = Widget.extend({
       xmlDependencies: ['/static/src/xml/collage_tamplate.xml'],  
       template: "collage_widget",   
        
        events: {
            "click .increment": 'onClickincrement',
            'click .decrement' : 'onClickdecrement',
            'click .destroy' : 'onClickdestroy'
        },

        init: function (parent, value) {
            this._super.apply(this, arguments);
            this.count = value;
        },

        onClickincrement: function () {
            this.count++;
            this.$('.count-number').val(this.count);
        },

        onClickdecrement : function () {
            this.count--;
            this.$('.count-number').val(this.count);
        },

        onClickdestroy : function()
        {
            this.destroy()

        }

});

core.action_registry.add('collage_action', collageTemplate);
    
    return collageTemplate;


});