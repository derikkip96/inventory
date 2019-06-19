(function($) {
    'use strict';
    var SelectBox = {
        cache: {},
        init: function(stock_id) {
            var box = document.getElementBystock_id(stock_id);
            var node;
            SelectBox.cache[stock_id] = [];
            var cache = SelectBox.cache[stock_id];
            var boxOptions = box.options;
            var boxOptionsLength = boxOptions.length;
            for (var i = 0, j = boxOptionsLength; i < j; i++) {
                node = boxOptions[i];
                cache.push({value: node.value, text: node.text, displayed: 1});
            }
        },
        redisplay: function(stock_id) {
            // Repopulate HTML select box from cache
            var box = document.getElementBystock_id(stock_id);
            var node;
            $(box).empty(); // clear all options
            var new_options = box.outerHTML.slice(0, -9);  // grab just the opening tag
            var cache = SelectBox.cache[stock_id];
            for (var i = 0, j = cache.length; i < j; i++) {
                node = cache[i];
                if (node.displayed) {
                    var new_option = new Option(node.text, node.value, false, false);
                    // Shows a tooltip when hovering over the option
                    new_option.setAttribute("title", node.text);
                    new_options += new_option.outerHTML;
                }
            }
            new_options += '</select>';
            box.outerHTML = new_options;
        },
        filter: function(stock_id, text) {
            // Redisplay the HTML select box, displaying only the choices containing ALL
            // the words in text. (It's an AND search.)
            var tokens = text.toLowerCase().split(/\s+/);
            var node, token;
            var cache = SelectBox.cache[stock_id];
            for (var i = 0, j = cache.length; i < j; i++) {
                node = cache[i];
                node.displayed = 1;
                var node_text = node.text.toLowerCase();
                var numTokens = tokens.length;
                for (var k = 0; k < numTokens; k++) {
                    token = tokens[k];
                    if (node_text.indexOf(token) === -1) {
                        node.displayed = 0;
                        break;  // Once the first token isn't found we're done
                    }
                }
            }
            SelectBox.redisplay(stock_id);
        },
        delete_from_cache: function(stock_id, value) {
            var node, delete_index = null;
            var cache = SelectBox.cache[stock_id];
            for (var i = 0, j = cache.length; i < j; i++) {
                node = cache[i];
                if (node.value === value) {
                    delete_index = i;
                    break;
                }
            }
            cache.splice(delete_index, 1);
        },
        add_to_cache: function(stock_id, option) {
            SelectBox.cache[stock_id].push({value: option.value, text: option.text, displayed: 1});
        },
        cache_contains: function(stock_id, value) {
            // Check if an item is contained in the cache
            var node;
            var cache = SelectBox.cache[stock_id];
            for (var i = 0, j = cache.length; i < j; i++) {
                node = cache[i];
                if (node.value === value) {
                    return true;
                }
            }
            return false;
        },
        move: function(from, to) {
            var from_box = document.getElementBystock_id(from);
            var option;
            var boxOptions = from_box.options;
            var boxOptionsLength = boxOptions.length;
            for (var i = 0, j = boxOptionsLength; i < j; i++) {
                option = boxOptions[i];
                var option_value = option.value;
                if (option.selected && SelectBox.cache_contains(from, option_value)) {
                    SelectBox.add_to_cache(to, {value: option_value, text: option.text, displayed: 1});
                    SelectBox.delete_from_cache(from, option_value);
                }
            }
            SelectBox.redisplay(from);
            SelectBox.redisplay(to);
        },
        move_all: function(from, to) {
            var from_box = document.getElementBystock_id(from);
            var option;
            var boxOptions = from_box.options;
            var boxOptionsLength = boxOptions.length;
            for (var i = 0, j = boxOptionsLength; i < j; i++) {
                option = boxOptions[i];
                var option_value = option.value;
                if (SelectBox.cache_contains(from, option_value)) {
                    SelectBox.add_to_cache(to, {value: option_value, text: option.text, displayed: 1});
                    SelectBox.delete_from_cache(from, option_value);
                }
            }
            SelectBox.redisplay(from);
            SelectBox.redisplay(to);
        },
        sort: function(stock_id) {
            SelectBox.cache[stock_id].sort(function(a, b) {
                a = a.text.toLowerCase();
                b = b.text.toLowerCase();
                try {
                    if (a > b) {
                        return 1;
                    }
                    if (a < b) {
                        return -1;
                    }
                }
                catch (e) {
                    // silently fail on IE 'unknown' exception
                }
                return 0;
            } );
        },
        select_all: function(stock_id) {
            var box = document.getElementBystock_id(stock_id);
            var boxOptions = box.options;
            var boxOptionsLength = boxOptions.length;
            for (var i = 0; i < boxOptionsLength; i++) {
                boxOptions[i].selected = 'selected';
            }
        }
    };
    window.SelectBox = SelectBox;
})(django.jQuery);
