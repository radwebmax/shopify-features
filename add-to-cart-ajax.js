let id = 36681942663331; //specify needed variant id
$.ajax({
type: 'POST',
url: '/cart/add.js',
data: {
  quantity: 1,
  id: id
},
dataType: 'json',
success: function (data) {
  console.log('Product added');
  setCookie('product', id);
  $('body').trigger('added.ajaxProduct');
  document.dispatchEvent(new CustomEvent('ajaxProduct:added'));
},
 error: function(){
     console.log('error', error)
 }
});
