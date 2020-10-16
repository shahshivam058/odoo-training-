odoo.define('openacademy.FieldIntegerRange', function (require) {
"use strict";

var basic_fields = require('web.basic_fields');
var FieldInteger = basic_fields.FieldInteger;
var field_registry = require('web.field_registry');

var FieldIntegerRange = FieldInteger.extend({

    _prepareInput: function () {
        var result = this._super.apply(this, arguments);
        this.$input.attr({type: 'range'});
        return result;
    },


});

field_registry.add('int_range', FieldIntegerRange);

return FieldIntegerRange;

});
