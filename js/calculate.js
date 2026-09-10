document.getElementById("calculadora").addEventListener("submit", function(event) {

    event.preventDefault();

    const numero1 = Number(document.getElementById("numero1").value);
    const numero2 = Number(document.getElementById("numero2").value);
    const operacao = document.getElementById("operacao").value;

    let resultado;

    if (operacao === "soma") {
        resultado = numero1 + numero2;
    }

    else if (operacao === "subtracao") {
        resultado = numero1 - numero2;
    }

    else if (operacao === "multiplicacao") {
        resultado = numero1 * numero2;
    }

    else if (operacao === "divisao") {

        if (numero2 === 0) {
            resultado = "Não é possível dividir por zero.";
        } else {
            resultado = numero1 / numero2;
        }

    }

    localStorage.setItem("resultado", resultado);

    window.location.href = "/result";
});
