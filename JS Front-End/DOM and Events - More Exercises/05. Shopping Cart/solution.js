function solve() {
   const addButtons = Array.from(document.getElementsByClassName('add-product'));
   const textArea = document.getElementsByTagName('textarea')[0];
   textArea.disabled = false;
   
   addButtons.forEach ((button) => {
      button.addEventListener('click', onAdd);
   });

   let totalSum = 0;
   let products = [];

   function onAdd(event) {
      const parentDiv = event.target.parentNode.parentNode;
      const nameProduct = parentDiv.querySelector('.product-details .product-title').textContent;
      const price = parentDiv.querySelector('.product-line-price').textContent;
      
      textArea.value += `Added ${nameProduct} for ${Number(price).toFixed(2)} to the cart.\n`;
      totalSum += Number(price);
      if (!products.includes(nameProduct)) {
         products.push(nameProduct);
      }
   }

   const btnCheckout = document.getElementsByClassName('checkout')[0];
   btnCheckout.addEventListener('click', onCheckout);

   function onCheckout() {
      textArea.value += `You bought ${products.join(', ')} for ${totalSum.toFixed(2)}.`
      addButtons.forEach((button) => button.disabled = true);
      btnCheckout.disabled = true;
   }     
}
