from string import Template  # se importa este modulo que permite reemplazar cosas a posterior. se puede generar una variable una dentro de otra cuanto sea necesario

# instantiate template
plantilla = Template(
    """

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de Chile</title>
    <!-- Bootstrap CSS -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .card {
            background-color: #c0e8f0;
        }

        .card-img {
            max-width: 300px;
            display: block;
            margin: 0 auto;
        }
    </style>
</head>

<body>

    <div class="container mt-4">
        <div class="row justify-content-center">
            <div class="col-4">
                <h1 class="text-center ">Aves de Chile</h1>


                $contenido

            </div>
        </div>
    </div>

    <!-- Script -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

</body>

</html>
                    """
)  # podria modificar algo de esto de manera dinamica.

plantilla_A = Template(
    """

                <div class="card my-4">
                    <div class="card-body">
                        <h2 class="card-subtitle mb-2 text-muted text-center">$name_esp</h2>
                        <h2 class="card-subtitle mb-2 text-muted text-center">$name_eng</h2>
                        <img src="$imagen_url"
                            width="300px" alt=$name_esp class="card-img">
                    </div>
                </div>
    """
)


