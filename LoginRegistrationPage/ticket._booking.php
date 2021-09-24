<?php

  session_start();

?>
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="cssfile/after_login.css">
    <link href="https://wbscc.wb.gov.in/assets/front_end/css/fontawsome.css" rel="stylesheet">
    <!-- Bootstrap CSS -->
    <link href="https://wbscc.wb.gov.in/assets/front_end/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">
    <link href="https://wbscc.wb.gov.in/assets/front_end/css/remixicon.css" rel="stylesheet">
    <link rel="stylesheet" href="https://wbscc.wb.gov.in/assets/front_end/css/style.css">
    <title>CYBER WORLD</title>
  </head>
 <body>
    <header>
      <div class="container">
        <div class="logo">
          <img src="photos\cyber_world.jpg">
          <div class="logo-text">
            <h1>CYBER WORLD</h1>
            <p>Department of All Online Saba<br> Govt. of West Bengal</p>
          </div>
        </div>
   
        <div class="support">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-telephone" viewBox="0 0 16 16">
                <path d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 1.77a17.568 17.568 0 0 0 4.168 6.608 17.569 17.569 
                0 0 0 6.608 4.168c.601.211 1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.678.678 0
                 0 0-.58-.122l-2.19.547a1.745 1.745 0 0 1-1.657-.459L5.482 8.062a1.745 1.745 0 0 1-.46-1.657l.548-2.19a.678.
                 678 0 0 0-.122-.58L3.654 1.328zM1.884.511a1.745 1.745 0 0 1 2.612.163L6.29 2.98c.329.423.445.974.315 1.494l-
                 .547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2
                 .306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 
                 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"/>
            </svg>
            <h4>8250771252</h4>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-envelope" viewBox="0 0 16 16">
                <path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 
                0-1-1H2zm13 2.383-4.758 2.855L15 11.114v-5.73zm-.034 6.878L9.271 8.82 8 9.583 6.728 8.82l-5.694 3.44A1 1 0 0 0 2 13h12a1 1 0 0
                0 .966-.739zM1 11.114l4.758-2.876L1 5.383v5.73z"/>
              </svg>
            <h4>rajandroprosad@gmail.com</h4>
            <!-- <h4><i class="ri-mail-fill"></i> rajandro@paytm.com</h4> -->
      </div>
    </div>
  </header>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
          <div class="navbar-nav">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
          <span>
          <a href="home.php"><button type="button" class="btn">Log Out</button></a>
          </span>
          </div>
        </div>
      </nav>

  <!-- <h1> Welcome <?php echo $_SESSION['uemail']; ?> </h1> -->

    <TABLE BORDER BGCOLOR=gray align="center">
        <TR> 
            <TH><FONT COLOR=WHITE FACE="Geneva, Arial" SIZE=6>ID<br></FONT></TH> 
            <TH><FONT COLOR=WHITE FACE="Geneva, Arial" SIZE=6>NAME<br></FONT></TH> 
            <TH><FONT COLOR=WHITE FACE="Geneva, Arial" SIZE=6>DESC<br></FONT></TH> 

        </TR>
        <TR>
            <TD><FONT COLOR=WHITE FACE="Geneva, Arial" SIZE=4>1</FONT></TD> 
            <TD><FONT COLOR=WHITE FACE="Geneva, Arial" SIZE=4>Flight</FONT></TD>
            <TD><a href="https://www.momondo.in/?ispredir=true"><FONT COLOR=WHITE FACE="Geneva, Arial" SIZE=4> momondo </FONT></a></TD> 
        </TR>
        <TR> 
            <TD><FONT COLOR=WHITE FACE="Geneva, Arial" SIZE=4>2</FONT></TD> 
            <TD><FONT COLOR=WHITE FACE="Geneva, Arial" SIZE=4>Train</FONT></TD>
            <TD><a href="https://www.irctc.co.in/nget/train-search"><FONT COLOR=WHITE FACE="Geneva, Arial" SIZE=4>IRCTC</FONT></a></TD>
        </TR>

        </TABLE>

<style>

</style>
</body>
</html>