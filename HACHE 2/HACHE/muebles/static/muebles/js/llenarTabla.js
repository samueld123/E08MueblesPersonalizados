function cargarDatos() {

    document.getElementById("idMueble").value =

        datos[registerPosition].entregable;

    document.getElementById("nombre").value =

        datos[registerPosition].precioProveedor;

    document.getElementById("estado").value =

        datos[registerPosition].precioCliente;

}

fetch("http://localhost:8080//traerTodoMuebles")
    .then((response) => response.json())

fetch("http://localhost:8080//traerNombresClientes", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            Accept: "application/json",
            "Content-type": "application/json",
        },
    })
    //===============================================================================================
    // function onFormSubmit() {
    //     var formData = readFormData();
    //     insertNewRecord(formData);
    //     resetForm();

// }

// function readFormData() {

//     var formData = {}

//     formData["Fecha"] = document.getElementById("fecha").value;
//     formData["Hora"] = document.getElementById("hora").value;
//     formData["Residuos"] = document.getElementById("residuos").value;
//     formData["CantidadU"] = document.getElementById("CantidadU").value;
//     formData["CantidadK"] = document.getElementById("CantidadK").value;
//     formData["Descripcion"] = document.getElementById("Descripcion").value;
//     return formData;

// }
//===============================================================================================

function insertNewRecord(data) {

    var table = document.getElementById("dataTable").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);

    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.Fecha;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.Hora;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.Residuos;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.CantidadU;
    cell5 = newRow.insertCell(4);
    cell5.innerHTML = data.CantidadK;
    cell6 = newRow.insertCell(5);
    cell6.innerHTML = data.Descripcion;



}