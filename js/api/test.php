<div class="container">
    <form action=<?=$_SERVER['REQUEST_URI']?> method="post">
        <p>How would you like die?<br>
            <br>
            <select name="Ingredients" required>
                <option value=0>[Choose Ingredient]</option>
                <option value=1>Rice</option>
                <option value=2>Milk</option>
                <option value=3>Sugar</option>
                <option value=4>Wheat</option>
                <option value=5>Soy</option>
            </select>
            <br>
            <br>
            <br>
            <select name="Diseases" required>
                <option value=0>[Choose Your Condition]</option>
                <option value=1>Obesity</option>
                <option value=2>Diabetes</option>
                <option value=3>Cardiovascular Disease</option>
                <option value=4>Cancer</option>
                <option value=5>Dental Disease</option>
                <option value=6>Osteoporosis</option>
            </select>
            <br>
            <br>
            <input type="submit" name="button" value="Submit" />
    </form>
</div>

<?php 
// use key 'http' even if you send the request to https://...
    $method = $_SERVER['REQUEST_METHOD'];
    if($method == 'POST'){

        $ingredients =  $_POST['Ingredients'];
        $disease = $_POST['Diseases'];
        
        // if($ingredients==0 or $disease == 0){
            
            
        // }

        
        $url = 'http://127.0.0.1:5000/postmsg/';
        $data = array('ingredients'=>$ingredients,'disease'=>$disease);
        $data = json_encode($data);
        print_r($data);
        
        $options = array(
            'http' => array(
                'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
                'method'  => 'POST',
                'content' => $data,
            ),
        );
        $context  = stream_context_create($options);
        $result = file_get_contents($url, false, $context);
        
if(!$result){
    echo('nope');
    echo('<br>');
}
else{
    echo($result);
}
if ($result === FALSE){
    echo("ffs");
    exit();
}
}
?>