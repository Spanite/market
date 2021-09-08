const copyBtn = document.getElementsByClassName('copy-btn')

let previous = null

copyBtn.forEach(btn => btn.addEventListner('click', ()=> {

  console.log('click')
  const color = btn.getAttribute('data')
  console.log('button')
  navigator.clipboard.writeText(color)
  btn.textContent = 'copied'

  navigator.clipboard.readText().then(clipText=>{
    console.log(clipText)
    btn.textContent = `copied ${clipText}`
  })

  if (previous){
    previous.textContent = 'click'
  }
  
}))