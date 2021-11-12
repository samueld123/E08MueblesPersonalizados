function validar() {
    var user = document.getElementById("InputUser").value;
    var password = document.getElementById("InputPassword").value;

    if (user == "juan" && password == "12345") {
        window.location.href = "index.html";
    } else {
        alert("No tiene los datos correctos")
    }
}