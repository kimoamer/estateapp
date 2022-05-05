// Copyright (c) 2022, test and contributors
// For license information, please see license.txt

frappe.ui.form.on('Property', {
  setup: function(frm){
    frm.check_amenities_duplicates = function (frm, row){
      frm.doc.amenities.forEach((item) => {
        if(row.amenity=='' || row.idx==item.idx){
        }else{
          if(row.amenity == item.amenity){
            frappe.msgprint(row.amenity);
            row.amenity = '';
            row.amenity_price = 0;
            row.discount = 0;
            frm.refresh_field('amenities');
          }
        }
      });
    },
    frm.compute_total = function (frm) {
      let total = frm.doc.property_price;
      if (frm.doc.discount && frm.doc.discount > 0){
        total = frm.doc.property_price - (frm.doc.property_price*(frm.doc.discount/100));
      }
      if (frm.doc.amenities){
        frm.doc.amenities.forEach(item => {
          let amenity_price = item.amenity_price - (item.amenity_price*(item.discount/100));
          total = total + amenity_price;
        });
      }
      frm.set_value("grand_total", total);
      frm.refresh_field("grand_total");
    }

  },
  // refresh: function (frm) {
  //   frm.chech_if_flat(frm);
  //   frm.add_custom_button("Check Property Type", ()=>{
  //     frappe.call({
  //       method: "estateapp.estateapp.doctype.property.api.check_property_type",
  //       args: {'property_type': frm.doc.property_type},
  //       callback: function(r) {
  //           console.log(r);
  //           if(r.message.length>0){
  //             let header = '<h3>Property Type is '+frm.doc.property_type+'</h3>';
  //             let body = '';
  //             r.message.forEach(item => {
  //               let cont = '<p>Name: '+item.property_type+' <a href="/app/property/'+item.name+'">Visit</a></p>';
  //               body = body + cont;
  //             });
  //             let all = header + body;
  //             frappe.msgprint(all);
  //           }
  //         }
  //       });
  //   });
  // },
  property_price: function (frm) {
    frm.compute_total(frm);
  },
  discount: function (frm) {
    frm.compute_total(frm);
  }

});

frappe.ui.form.on('Property Amenity Details', {
  amenity: function(frm, cdt, cdn){
    let row = locals[cdt][cdn];
    frm.check_amenities_duplicates(frm, row);
    frm.compute_total(frm);
  },
  amenities_remove: function(frm){
    frm.compute_total(frm);
  }
});
