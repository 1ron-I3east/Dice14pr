<html>

<head>
    <title>HTML Service</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jost">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <style>
        body {
            font-family: "Jost", sans-serif;
            color: white;
            background: no-repeat;
            background-size: 100%;
            background-image: url('https://phonoteka.org/uploads/posts/2022-01/thumbs/1642976756_5-phonoteka-org-p-zadnii-fon-dlya-saita-5.jpg');
        }

        /* 
        .container {
            border: 4px solid white;
            border-radius: 15px;
            background-color: rgb(26, 26, 26);
            margin-top: 15px;
            margin-left: auto;
            margin-right: auto;
        }
        .list-group .list-group-item {
            margin-top: 5px;
            border: 1px solid black;
            border-radius: 15px;
            color: black;
        }
        .form-control.form-control-lg {
            border: 2px solid black;
            border-radius: 15px;
        }
        .btn.btn-info {
            border: 2px solid white;
            border-radius: 15px;
        } */
    </style>
</head>

<body>
    <div class="container form">
        <div class="container-fluid">
            <h2 style="margin-left:50%">Статистика персонажа</h2>
        </div>


        <form action="index.php" method="post">
            <input type="hidden" name="output" id="output" value=1>
            <button type="submit" class="btn btn-info" style=" margin-left:50%">Вывод</button>
        </form>
        <form action="index.php" method="post">
            <input type="hidden" name="download" id="download" value=1>
            <button type="submit" class="btn btn-info"  style=" margin-left:50%">скачать</button>
        </form>
        <form action="index.php" method="post">
            <input type="hidden" name="create" id="create" value=1>
            <button type="submit" class="btn btn-info"  style=" margin-left:50%">создать</button>
        </form>
    </div>
    <br><br>
    <table class="table">
       
            <?php
            if (isset($_POST['create'])) {
                $myCurl = curl_init();
                curl_setopt_array(
                    $myCurl,
                    array(
                        CURLOPT_URL => 'http://nginxserver/test/',
                        CURLOPT_RETURNTRANSFER => true,
                        CURLOPT_HEADER => false,
                    )
                );
                echo '<thead>
                <th>ExcelId</th>
                <th>Id</th>
                <th>Name</th>
                <th>Hero</th>
                <th>Race</th>
                <th>Strength</th>
                <th>Constitution</th>
                <th>Dexterity</th>
                <th>Intelligence</th>
                <th>Wisdom</th>
                <th>Charisma</th>
                </thead>
                <tbody>';
                $response = curl_exec($myCurl);
                curl_close($myCurl);
                $json = json_decode($response, true);
                $zadacha = $json['zadacha'];
                for ($i = 0; $i <= count($zadacha['name']); $i++) {
                    // $zadacha as $value
                    echo "<tr>";
                    foreach ($zadacha as $key => $value) {
                        
                        echo "<td>" .  $value[$i] . "</td>";
                    }
                    echo "</tr>";
                }
            }
            ?>
        </tbody>
    </table>
    <?php

    if (isset($_POST['output'])) {
        // $output_filename = "character.txt";
        $myCurl = curl_init();
        curl_setopt_array(
            $myCurl,
            array(
                CURLOPT_URL => 'http://nginxserver/main/',
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_HEADER => false,
                // CURLOPT_AUTOREFERER => false,
                // CURLOPT_REFERER => 'http://nginxserver'
            )
        );
        $response = curl_exec($myCurl);

        curl_close($myCurl);
        echo $response;
    }
    if (isset($_POST['download'])) {

        $output_filename = "character.xlsx";


        $myCurl = curl_init();
        curl_setopt_array(
            $myCurl,
            array(
                CURLOPT_URL => 'http://nginxserver/download/',
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_HEADER => false,

                // CURLOPT_AUTOREFERER => false,
                // CURLOPT_REFERER => 'http://nginxserver'
            )
        );
        $response = curl_exec($myCurl);
        $fp = fopen($output_filename, 'wb');
        fwrite($fp, $response);
        fclose($fp);
        curl_close($myCurl);
        ob_end_clean();
        header('Content-Description: File Transfer');
        header('Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet');
        header("Cache-Control: must-revalidate");
        header('Content-Transfer-Encoding: Binary');
        header("Expires: 0");
        header('Content-Disposition: attachment; filename="' . basename($output_filename) . '"');
        header('Content-Transfer-Encoding: binary');
        header('Content-Length: ' . filesize($output_filename));
        header('Pragma: public');
        readfile($output_filename);
        // echo $response;
    }
    // if (isset($_POST['create'])) {
    //     // $output_filename = "character.txt";
    //     $myCurl = curl_init();
    //     curl_setopt_array(
    //         $myCurl,
    //         array(
    //             CURLOPT_URL => 'http://nginxserver/test/',
    //             CURLOPT_RETURNTRANSFER => true,
    //             // CURLOPT_FOLLOWLOCATION => true,
    //             CURLOPT_HEADER => false,
    //             // CURLOPT_AUTOREFERER => false,
    //             // CURLOPT_REFERER => 'http://nginxserver'
    //         )
    //     );
    //     // header('Content-Type: application/json');
    //     $response = curl_exec($myCurl);
    //     curl_close($myCurl);
    //     // echo $response;
    //     $json = json_decode($response, true);

    //     // echo $response;
    //     // var_dump($json);
    //     // $url = $json->url;
    //     $zadacha = $json['zadacha'];
    //     foreach ($zadacha as $value) {
    //         // echo $value . ' ';
    //         echo "<tr>";
    //         foreach ($value as $value2) {
    //             echo "<td>" .  $value2 . "</td>";
    //         }
    //         echo "</tr>";
    //     }
    //     // echo $url;
    //     // echo $zadacha;
    //     // // $array = $json->text;
    //     // foreach ($response as $value) {
    //     //     echo "<tr>";
    //     //     foreach ($numbers as $number) {
    //     //       echo "<td>" . $number . "</td>";
    //     //     }
    //     //     echo "</tr>";
    //     //   }

    // }
    ?>
</body>

</html>