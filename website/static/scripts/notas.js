function mapearNotas(inputs) {
    let notas = []

    inputs.forEach(function(input){
        notas.push(parseFloat(input.value || 0))
    })

    return notas
}

function calculaMac(notasAcs) {
    let mac = 0, quantidadeAcs = notasAcs.length

    for(let i = 0; i < quantidadeAcs; i++){
        mac += notasAcs[i]
    }

    mac = mac / quantidadeAcs

    return (mac * 0.6).toFixed(2)
}

function calculaMp(notas){
    let maximo = 0
    
    notas.forEach(function(nota){
        maximo = nota >= maximo ? nota : maximo
    })

    return (maximo * 0.4).toFixed(2)
}

function pegaLinhaPai($td){
    return $td.parentElement.parentElement
}

function setaNotaMac() {
    let linhaPai = pegaLinhaPai(this),
    inputAcs = linhaPai.querySelectorAll("td.ac input"),
    notas = mapearNotas(inputAcs)

    linhaPai.querySelector("td.mac").textContent = calculaMac(notas)
    setaNotaFinal(linhaPai)
}

function setaMaxProva(){
    let linhaPai = pegaLinhaPai(this),
    inputProvas = linhaPai.querySelectorAll('td.prova input'),
    notas = mapearNotas(inputProvas)

    linhaPai.querySelector('td.mp').textContent = calculaMp(notas)
    setaNotaFinal(linhaPai)
}

function setaNotaFinal(linhaPai){
    let mac = parseFloat(linhaPai.querySelector('td.mac').textContent),
    mp = parseFloat(linhaPai.querySelector('td.mp').textContent),
    tdFinal = linhaPai.querySelector('td.final'),
    notaFinal = (mp + mac).toFixed(2)

    tdFinal.textContent = notaFinal
    if(notaFinal >= 6){
        tdFinal.classList.remove('reprovado')
        tdFinal.classList.add('aprovado')
    } else {
        tdFinal.classList.add('reprovado')
        tdFinal.classList.remove('aprovado')
    }
}

function criarInputAc(numAc){
    let input = document.createElement('input')

    input.type = 'number'
    input.name = 'ac'+numAc
    input.value = "0.0" 
    input.step = "0.01"
    input.classList.add("input-nota")
    input.min="0"
    input.max="10"
    input.required = true

    input.addEventListener('change', setaNotaMac)

    return input
}

function adicionarAC() {
    let thAcs = document.querySelector('th.acs'),
    ths = document.querySelector('thead tr:nth-child(2)'),
    numAcs = ths.querySelectorAll('th.ac').length+1,
    trs = document.querySelectorAll('table tbody tr')

    if (numAcs > 10){
        alert('São permitidos no máximo 10 ACs')
        return
    }

    let th = document.createElement('th')
    th.classList.add('nota')
    th.classList.add('ac')
    th.textContent = 'AC'+numAcs
    ths.insertBefore(th, ths.querySelector('th.mac'))

    thAcs.colSpan = numAcs

    trs.forEach(function(tr){
        let td = document.createElement('td'),
        tdMac = tr.querySelector('td.mac'),
        input = criarInputAc(numAcs)
        td.classList.add("nota")
        td.classList.add("ac")
        td.appendChild(input)
        tr.insertBefore(td, tdMac)
    })

}

function removerAluno(){
    let tr = pegaLinhaPai(this)
    if(document.querySelectorAll('table tbody tr').length == 1){
        alert("Ao menos um aluno é obrigatório")
        return
    }
    tr.remove()
}

function adicionarAluno(nome, ra) {
    let tbody = document.querySelector('table tbody'),
    lastTr = tbody.lastElementChild,
    clone = lastTr.cloneNode(true)

    clone.querySelector("td.ra").textContent = ra
    clone.querySelector("td.nome").textContent = nome

    clone.querySelector("td.mac").textContent = 0.0
    clone.querySelector("td.mp").textContent = 0.0
    clone.querySelector("td.final").textContent = 0.0

    clone.querySelector("button.remover-aluno").addEventListener('click', removerAluno)

    clone.querySelectorAll("td.ac input").forEach(function(input){
        input.value = 0.0
        input.addEventListener('change', setaNotaMac)
    })

    clone.querySelectorAll("td.prova input").forEach(function(input){
        input.value = 0.0
        input.addEventListener('change', setaMaxProva)
    })

    tbody.appendChild(clone)
}
const acs = document.querySelectorAll('td.ac input')
const provas = document.querySelectorAll('td.prova input')
const adicionarAc = document.querySelector('button.adicionar-ac')
const removeAluno = document.querySelector('button.remover-aluno')
const adicionaAluno = document.querySelector('button.adicionar-aluno')

adicionarAc.addEventListener('click', adicionarAC)

removeAluno.addEventListener('click', removerAluno)

adicionaAluno.addEventListener('click', function(){
    let inputNome = document.querySelector('input[name="nome"]'),
    nome = inputNome.value,
    inputRa = document.querySelector('input[name="ra"]'),
    ra = inputRa.value
    if(nome && ra){
        adicionarAluno(nome, ra)
        inputNome.value = ''
        inputRa.value = ''
    }
})

acs.forEach(function(ac){
    ac.addEventListener('change', setaNotaMac)
})

provas.forEach(function(prova){
    prova.addEventListener('change', setaMaxProva)
})