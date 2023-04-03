function createElement(type, parentNode, content, classes, id, attributes, useInnerHtml) {
    const htmlElement = document.createElement(type);
  
    if (content && useInnerHtml) {
      htmlElement.innerHTML = content;
    } else {
      if (content && type !== 'input') {
        htmlElement.textContent = content;
      }
  
      if (content && type === 'input') {
        htmlElement.value = content;
      }
    }
  
    if (classes && classes.length > 0) {
      htmlElement.classList.add(...classes);
    }
  
    if (id) {
      htmlElement.id = id;
    }
  
    // { src: 'link', href: 'http' }
    if (attributes) {
      for (const key in attributes) {
        htmlElement.setAttribute(key, attributes[key])
      }
    }
  
    if (parentNode) {
      parentNode.appendChild(htmlElement);
    }
  
    return htmlElement;
  }
  

  

// ** SECOND **
  
//   function createElement(type, content, parentNode, id, classes, attributes){
//   const htmlElement = document.createElement(type)

//   if(content && type !== 'input'){
//     htmlElement.textContent = content;
//   }

//   if(content && type === 'input'){
//     htmlElement.value = content;
//   }

//   if(id){
//     htmlElement.id = id;
//   }

//   if (classes){
//     htmlElement.classList.add(...classes);
//   }

//   if (parentNode){
//     parentNode.appendChild(htmlElement);
//     }

//   //{ src: 'link to img', href: 'link to site' }
//   if (attributes){
//     for (const key in attributes) {
//       htmlElement.setAttribute(key, attributes[key]); 
//     }
//   } 
//   return htmlElement
// }
  
