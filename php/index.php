<?php 
$host = 'db';
$user = 'phpmyadmin';
$password = 'samarinda';
$db = 'test_db';

$conn = new mysqli($host, $user, $password, $db);
if($conn->connect_error){
  echo 'koneksi gagal'. $conn->connect_error;
}

echo 'koneksi berhasil';