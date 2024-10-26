function main() {
    let nroPagina = document.querySelector('#nro-pagina').innerHTML
    let linkPrevious = document.querySelector('#enlace-anterior')
    let linkNext = document.querySelector('#enlace-siguiente')
    
    //Página anterior
    let paginaAnterior = Number(nroPagina) - 1
    let rutaAnterior = `/previous/` 
    linkPrevious.setAttribute('href', `${rutaAnterior}${paginaAnterior}`)
    
    //Página siguiente
    let paginaSiguiente = Number(nroPagina) + 1
    let rutaSiguiente = `/next/` 
    linkNext.setAttribute('href', `${rutaSiguiente}${paginaSiguiente}`)
    
    if (paginaAnterior == 0) {
        linkPrevious.setAttribute('href', '#')
    }
}

document.addEventListener("DOMContentLoaded", main)