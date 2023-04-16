import { docQueryAll } from './utils.js'

// функция по нажатию на элемент отображает элемент с классом on-click-unfold--modal
// 
const onClickUnfold = (main, modal) => {
    const mains = docQueryAll(main)
    const modals = docQueryAll(modal)

    // const styles = () => {
    //     document
    // }

    const onClickLogic = (main, modal) => {
        main.addEventListener('click', () => {
            modal.style.right = 0

            modal.style.width = '200px'
            modal.style.height = '100px'
        })

        modal.addEventListener('mouseout', () => {
            modal.style.width = 0
            modal.style.height = 0
        })
    }

    for(let M = 0; M < mains.length; M++) {
        console.log(mains[M])

        onClickLogic(mains[M], modals[M])

    } // for T
}

onClickUnfold('.on-click-unfold', '.on-click-unfold--modal')
