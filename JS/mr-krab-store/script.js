
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

async function changeDisplay (){
  const responseMenu = await fetch('http://localhost:8000/menu')
  if (!responseMenu.ok){
    console.log('Failed to load data')
  }
  const menuData = await responseMenu.json()
  console.log('here')
  const change = await gifToMenu(menuData)
  console.log('jdfk')
  
}

function gifToMenu (jsonMenu){
  document.getElementById('loader').hidden = true

  for (let item in jsonMenu['items']){
    console.log(item)
    console.log(jsonMenu['items'][item])
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

    const quantity = document.createElement('input')
    quantity.setAttribute('type', 'currency')
    quantity.setAttribute('id', 'currency-field')
    quantity.setAttribute('name', 'currency-field')

    const menuItem = document.createElement('span')
    menuItem.setAttribute('class', 'item')

    menuItem.appendChild(title)
    menuItem.appendChild(pDescription)
    menuItem.appendChild(label)
    menuItem.appendChild(quantity)

    menu.appendChild(menuItem);
  }
}

const menu = document.getElementById("menu");

window.addEventListener('load', changeDisplay);