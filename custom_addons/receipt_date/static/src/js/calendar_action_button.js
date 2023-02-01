odoo.define('reciept_date.PurchasePortalSidebarAction', function (require) {
'use strict';

console.log("Receipt date js run");

var publicWidget = require('web.public.widget');
var PortalSidebar = require('portal.PortalSidebar');
const core = require('web.core');
const QWeb = core.qweb;
const time = require('web.time');

console.log("New Receipt date js run");

    publicWidget.registry.PurchasePortalSidebarCalendar = PortalSidebar.extend({

        selector: '.o_portal_purchase_sidebar',
        events: {
            'click .o_calendar_btn': '_onClick',
        },

        _onClick: async function (ev) {
        debugger;
            var self = this;
            console.log("This is a self", self);

            $("#calendar_date").datetimepicker({
                dateFormat: "yyyy-MM-dd"
            });

            var poId = $(ev.currentTarget).data('po-id');
            var access_token = $(ev.currentTarget).data('access');
            var poDate = $(ev.currentTarget).data('po-date');

            this.$createModal = $(QWeb.render(
                'calendar_view',
                {
                    csrf_token: odoo.csrf_token,
                    order_id : poId,
                    receipt_date: poDate,
                    access_token : access_token

                }
            ));
            this.$createModal.appendTo(this.$el.parentNode);

            this.$createModal.modal('show');

        }
    });
});














//Workin:

//odoo.define('reciept_date.PurchasePortalSidebarAction', function (require) {
//'use strict';
//
//console.log("Receipt date js run");
//
//var publicWidget = require('web.public.widget');
//var PortalSidebar = require('portal.PortalSidebar');
//const core = require('web.core');
//const QWeb = core.qweb;
//
//console.log("New Receipt date js run");
//
//    publicWidget.registry.PurchasePortalSidebarCalendar = PortalSidebar.extend({
//
//        selector: '.o_portal_purchase_sidebar',
//        events: {
//            'click .o_calendar_btn': '_onClick',
//        },
//
//        _onClick: async function () {
//        debugger;
//            var self = this;
//            console.log("This is a self", self);
//
//            console.log("Function run");
//            console.log("Token id-",window.location.href)
//            var url = window.location.href.split("/")[5].replace("=", "?").split("?");
//            console.log(url);
//
//            this.$createModal = $(QWeb.render(
//                'calendar_view',
//                {
//                    csrf_token: odoo.csrf_token,
//                    order_id: url[0],
//                    access_token: url[2],
//                }
//            ));
//            this.$createModal.appendTo(this.$el.parentNode);
//
//            this.$createModal.modal('show');
//
//        }
//    });
//});
