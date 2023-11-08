
/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }

*/

fetch('http://localhost:8000/menu')
  .then(res => res.json())
  .then(data => console.log(data))

async function changeDisplay() {
  const responseMenu = await fetch('http://localhost:8000/menu')
  if (!responseMenu.ok) {
    console.log('Failed to load data')
  }
  const menuData = await responseMenu.json()
  const hideImg = await hideGif()
  const change = await gifToMenu(menuData)
  const summary = await displaySummary()
}

function hideGif() {
  img = document.getElementById('loader')
  img.setAttribute('src', '')
}

function gifToMenu(jsonMenu) {
  for (let item in jsonMenu['items']) {
    let description = jsonMenu['items'][item]['description']
    let name = jsonMenu['items'][item]['name']
    let price = jsonMenu['items'][item]['price']

    const title = document.createElement('h3')
    title.innerText = `${name} ($${price.toFixed(2)})`

    const pDescription = document.createElement('p')
    pDescription.innerText = description

    const label = document.createElement('label')
    label.innerText = 'quantity: '
    label.setAttribute('for', 'currency-field')
    label.setAttribute('class', 'input-group')

    const quantity = document.createElement('input')
    quantity.setAttribute('type', 'currency')
    quantity.setAttribute('id', 'currency-field')
    quantity.setAttribute('name', 'currency-field')
    quantity.setAttribute('class', 'input-group')
    quantity.setAttribute('value', 0)
    quantity.setAttribute('placeholder', '0')
    quantity.setAttribute('max', '5')

    const menuItem = document.createElement('span')
    menuItem.classList.add('item')
    menuItem.setAttribute('id', 'latest-order-info')

    menuItem.appendChild(title)
    menuItem.appendChild(pDescription)
    menuItem.appendChild(label)
    menuItem.appendChild(quantity)

    menu.appendChild(menuItem);
  }
}

function orderSummary() {
  const itemArr = menu.getElementsByTagName('span')
  summary.querySelectorAll('span').forEach(meal => meal.remove())

  for (let item = 0; item < itemArr.length; item++) {
    const itemQuantity = itemArr[item].childNodes[3]
    const title = itemArr[item].querySelector('h3').textContent

    if (itemQuantity.value > 0) {
      summary.querySelector('p').innerText = ''
      const addItem = document.createElement('span')
      let name = title.split('(')[0]
      let price = title.split('(')[1].split('$')[1].split(')')[0]
      console.log(name)
      console.log(price)
      addItem.innerText = `${name} (${itemQuantity.value} x ${price} = ${price * itemQuantity.value})\n`
      summary.appendChild(addItem)
    }
  }
}

function displaySummary(){
  const input = document.getElementsByName('currency-field')
  input.forEach(function(element) {
    if(element.addEventListener('input', orderSummary)){
      return;
    }
  });
}

const menu = document.getElementById("menu");
const summary = document.getElementById('order-summary')
const lineBreak = document.createElement('BR');

window.addEventListener('load', changeDisplay);