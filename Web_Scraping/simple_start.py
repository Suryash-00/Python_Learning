from bs4 import BeautifulSoup

SIMPLE_HTML= '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fitian</title>
</head>
<link rel="stylesheet" href="css/style.css">
<style>
    /* CSS Reset */
    body {
        color: whitesmoke;
        margin: 0px;
        padding: 0px;
        background: url('images/bg.jpg');
        height: 855px;
    }

    .left {
        display: inline-block;
        position: absolute;
        left: 40px;
        top: 12px;
        /*border: 2px solid coral; */
        font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    }

    .left img {
        width: 75px;
        height: 50px;
        border-radius: 50px;
    }

    .left div {
        text-align: center;
        font-size: 18px;
        line-height: 15px;
    }

    .mid {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        display: block;
        width: 33%;
        margin: 12px auto;
        /* border: 2px solid steelblue; */
    }

    .right {
        position: absolute;
        right: 40px;
        top: 12px;
        display: inline-block;
        /*border: 2px solid indianred; */
    }

    .navbar {}

    .navbar li {
        display: inline-block;
        font-size: 15px;
    }

    .navbar li a {
        color: whitesmoke;
        text-decoration: none;
        padding: 12px 10px;
    }

    .navbar li a:hover {
        color: darkgray;
        text-decoration: none;
    }

    .btn {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        margin-right: 8px;
        padding: 10px 15px;
        border-radius: 5px;
        cursor: pointer;
    }

    .btn:hover {
        background-color: darkgray;
    }

    .container {
        font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
        background: url('images/winning.jpg');
        border: 2px solid aquamarine;
        margin: 100px 120px;
        padding: 50px 50px;
        width: 35%;
        border-radius: 10px;
        background-size: 500px;
    }

    .form_group input {
        border-radius: 8px;
        margin: 5px auto;
        width: 300px;
    }
</style>

<body>
    <header class="header">
        <div class="left">
            <img src="images/logo.jpg" alt="">
            <div>Fitian</div>
        </div>
        <div class="mid">
            <ul class="navbar">
                <li><a href="#">Home</a></li>
                <li><a href="#">About Us</a></li>
                <li><a href="#">Our Centres</a></li>
                <li><a href="#">Contact Us</a></li>
            </ul>
        </div>
        <div class="right">
            <button class="btn">Join Us</button>
            <button class="btn">Get a call</button>
        </div>
    </header>
    <div class="container">
        <h1>Become a Fitian now!</h1>
        <form action="noaction.php">
            <div class="form_group">
                <input type="text" name="" placeholder="Enter your name">
            </div>
            <div class="form_group">
                <input type="text" name="" placeholder="What's your age?">
            </div>
            <div class="form_group">
                <input type="text" name="" placeholder="Gender?">
            </div>
            <div class="form_group">
                <input type="text" name="" placeholder="Please enter your location">
            </div>
            <button class="btn">Let's Go--></button>
        </form>
    </div>
</body>

</html>
'''
simple_soup= BeautifulSoup(SIMPLE_HTML, 'html.parser')

print(simple_soup.find('h1').string)

list_items= simple_soup.find_all('li')
list_contents= [e.string for e in list_items]
print(list_contents)

paragraph= simple_soup.find('p', {'class': 'btn'})
print(paragraph)

other_paragraph=[p for p in paragraph if 'btn' not in p.attrs.get('class', [])]
print(other_paragraph)