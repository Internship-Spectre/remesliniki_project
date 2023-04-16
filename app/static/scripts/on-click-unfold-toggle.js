import { docQueryAll } from './utils.js'

// функция по нажатию на элемент отображает элемент с классом on-click-unfold-toggle--modal
const onClickUnfoldToggle = (main, modal) => {

    // выбирает все элементы с указанным классом
    const mains = docQueryAll(main)
    const modals = docQueryAll(modal)

    // логика приложения на нажатие
    const onClickLogic = (main, modal) => {

        // дефолтное состояние модалки(невидно) 
        let state = false

        main.addEventListener('click', () => {
            
            if(state === false) {
                modal.style.right = 0
                
                modal.style.width = '200px'
                modal.style.height = '100px'
                state = true
            }
            
            else if(state === true) {
                modal.style.width = 0
                modal.style.height = 0
                state = false
            }
        })
    } // fun onClickLogic

    for(let M = 0; M < mains.length; M++) {
        console.log(mains[M])

        onClickLogic(mains[M], modals[M])

    } // for T
} // fun onClickUnfoldToggle

// запускает скрипт прикрепленный к странице
onClickUnfoldToggle('.on-click-unfold-toggle', '.on-click-unfold-toggle--modal')
