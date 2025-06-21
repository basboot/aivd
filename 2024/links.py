from bs4 import BeautifulSoup

p1 = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <title>MLDb, The Music Lyrics Database - Advanced search</title>
    <meta name="Author" content="Nikolay Pelov, NickSoft"/>
    <meta name="Description" content="MLDb - Advanced search. Searching for &amp;quot;a million&amp;quot;"/>
    <meta name="Keywords" content="music,song,lyrics,mldb"/>
    <meta name="robots" content="index,follow"/>
    <meta name="revisit-after" content="7 days"/>
    <meta name="title" content="MLDb, The Music Lyrics Database - Advanced search"/>
    <meta name="distribution" content="Global"/>
    <meta name="rating" content="general"/>
    <link href="style.css" media="all" type="text/css" rel="stylesheet"/>
    <link href="/favicon.ico" rel="shortcut icon"/>
    <link rel="search" type="application/opensearchdescription+xml" href="http://www.mldb.org/opensearch.xml" title="MLDb music lyrics search"/>
    <!-- music song lyrics database begins -->
    <!-- music song lyrics database navigation links -->
    <link rel="MLDb - Home" title="Music lyrics" href="http://www.mldb.org/"/>
    <link rel="section" title="Music lyrics Search" href="http://www.mldb.org/search"/>
    <link rel="section" title="Top 40 Music Lyrics" href="http://www.mldb.org/top40.html"/>
    <link rel="section" title="Latest Music Lyrics" href="http://www.mldb.org/new-lyrics.html"/>
    <link rel="section" title="Submit music lyrics to database" href="http://www.mldb.org/submit.html"/>
    <link rel="contents" title="Extras: toolbar buttons, firefox search box" href="http://www.mldb.org/extras.html"/>
    <style type="text/css">
        <!--
        .dnone{
          display:none;
        }
        -->
        
    </style>
    <!-- International portal to music lyrics. Sorted lyrics by artist name. Clean and easy-to-use site with over 220,000 lyrics -->
    <!-- Top 40 lyrics chart. Comprehensive music lyrics search engine. Fulltext lyrics search. Search by artist, title, both of them or song lyrics -->
    <!-- <link rel="prefetch" href="http://"> -->
    <script type="text/javascript" src="js/main.js?v=3"></script>
    <script type="text/javascript" src="/js/ST.min.js?v=2"></script>
</head>
<body style="margin: 0px; padding: 0px;">
    <center>
        <div id="container">
            <table id="toptbl" align="center" cellspacing="0">
                <tr>
                    <td>
                        <!--<img src='img/headerbg.png' id="topimg" />-->
                        <div id="topadframe">
                            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9307576326974516" crossorigin="anonymous"></script>
                            <!-- MLDb top 468x60 -->
                            <ins class="adsbygoogle" style="display:inline-block;width:468px;height:60px" data-ad-client="ca-pub-9307576326974516" data-ad-slot="9720604683"></ins>
                            <script>
                            (adsbygoogle = window.adsbygoogle || []).push({});
                            </script>
                        </div>
                        <div id="toplinks" style="width:200px;position:absolute;">
                            <a href="/advertise.html" style="color:orange">Advertise</a>
                            <a href='/contact.html'>contact us</a>
                        </div>
                        <div style="height:80px"></div>
                        <div id="nav">
                            <div style="height:6px">
                                <img alt="" src="img/spacer.gif" width="1" height="6"/>
                            </div>
                            <div id="tabs" align="left">
                                <ul>
                                    <li>
                                        <a href="/" title="Music Lyrics Database Homepage">home</a>
                                    </li>
                                    <li>
                                        <a href="/aza-A.html" title="Complete artist list">artists</a>
                                    </li>
                                    <li>
                                        <a href="/azl-A.html" title="Complete album list">albums</a>
                                    </li>
                                    <li>
                                        <a href="/search?v=3" title="Search for song lyrics, detailed search" class="active">search</a>
                                    </li>
                                    <li>
                                        <a href="/top40.html" title="Top Chart of Music Lyrics Database">top 40</a>
                                    </li>
                                    <li>
                                        <a href="/new-lyrics.html" title="New lyrics">new</a>
                                    </li>
                                    <li>
                                        <a href="/submit.html" title="Submit new lyrics - help to make the world biggest music lyrics collection" style="color:#FFE090;">submit</a>
                                    </li>
                                    <li>
                                        <a href="/extras.html" title="Browser toolbars, buttons, search boxes." style="border-right: 1px solid rgb(119, 119, 119);">extras</a>
                                    </li>
                                </ul>
                            </div>
                            <div class="underline">
                                <img src="img/spacer.gif" alt="Main menu" height="2" width="1"/>
                            </div>
                            <!--  <div style="border-left: 1px solid rgb(119, 119, 119); float: left; height: 1px;"></div>-->
                            <div id="ajaxNav">
                                <div id="az" class="slip">
                                    <ul>
                                        <li>
                                            <a href="aza-0.html">#</a>
                                            <a href="aza-A.html">A</a>
                                            <a href="aza-B.html">B</a>
                                            <a href="aza-C.html">C</a>
                                            <a href="aza-D.html">D</a>
                                            <a href="aza-E.html">E</a>
                                            <a href="aza-F.html">F</a>
                                            <a href="aza-G.html">G</a>
                                            <a href="aza-H.html">H</a>
                                            <a href="aza-I.html">I</a>
                                            <a href="aza-J.html">J</a>
                                            <a href="aza-K.html">K</a>
                                            <a href="aza-L.html">L</a>
                                            <a href="aza-M.html">M</a>
                                            <a href="aza-N.html">N</a>
                                            <a href="aza-O.html">O</a>
                                            <a href="aza-P.html">P</a>
                                            <a href="aza-Q.html">Q</a>
                                            <a href="aza-R.html">R</a>
                                            <a href="aza-S.html">S</a>
                                            <a href="aza-T.html">T</a>
                                            <a href="aza-U.html">U</a>
                                            <a href="aza-V.html">V</a>
                                            <a href="aza-W.html">W</a>
                                            <a href="aza-X.html">X</a>
                                            <a href="aza-Y.html">Y</a>
                                            <a href="aza-Z.html">Z</a>
                                            <a href="aza-_.html">*</a>
                                        </li>

                                    </ul>
                                </div>
                            </div>
                        </div>
                    </td>
                </tr>
            </table>
            <table id="centertbl" align="center" cellspacing="0">
                <tr>
                    <td colspan="2" class="center">
                        <!-- page IS safe center -->
                        <div style="width:728px;height:90px;margin:auto">
                            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9307576326974516" crossorigin="anonymous"></script>
                            <!-- MLDb below top nav 728x90 -->
                            <ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-9307576326974516" data-ad-slot="5179889214"></ins>
                            <script>
                            (adsbygoogle = window.adsbygoogle || []).push({});
                            </script>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td class="leftplane">
                        <div style="width:160px">
                            <!-- Left Nav -->
                            <script type="text/javascript">
                            searchBox();
                            </script>
                            <br/>
                            <br/>
                            <script type="text/javascript">
                            drawStats(236679, 24057, 11223, 183);
                            </script>
                            <br/>
                            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9307576326974516" crossorigin="anonymous"></script>
                            <!-- MLDB Left Sidebar 160x600 -->
                            <ins class="adsbygoogle" style="display:inline-block;width:160px;height:600px" data-ad-client="ca-pub-9307576326974516" data-ad-slot="7838877680"></ins>
                            <script>
                            (adsbygoogle = window.adsbygoogle || []).push({});
                            </script>
                            <br/>
                            <br/>
                            <table class="main_tbl" cellspacing="0" style="width:160px">
                                <thead>
                                    <tr>
                                        <td>Top artists</td>
                                    </tr>
                                </thead>
                                <tr>
                                    <td>
                                        <a href='artist-3796-a-funny-thing-happened-on-the-way-to-the-forum-soundtrack.html?nc=1'>A Funny Thing Happened on the Way to the Forum Soundtrack</a>
                                        <br/>
                                        <a href='artist-25-metallica.html?nc=1'>Metallica</a>
                                        <br/>
                                        <a href='artist-278-a.html?nc=1'>A</a>
                                        <br/>
                                        <a href='artist-3795-a-charlie-brown-christmas-soundtrack.html?nc=1'>A Charlie Brown Christmas Soundtrack</a>
                                        <br/>
                                        <a href='artist-3807-fame-soundtrack.html?nc=1'>Fame Soundtrack</a>
                                        <br/>
                                    </td>
                                </tr>
                            </table>
                            <br/>
                            <table class="main_tbl" cellspacing="0" style="width:160px">
                                <thead>
                                    <tr>
                                        <td>Top albums</td>
                                    </tr>
                                </thead>
                                <tr>
                                    <td>
                                        <a href='album-12771-a-funny-thing-happened-on-the-way-to-the-forum-soundtrack.html?nc=1'>A Funny Thing Happened on the Way to the Forum Soundtrack</a>
                                        <br/>
                                        <a href='album-21665-a-arte-de-leila-pinheiro.html?nc=1'>A Arte de Leila Pinheiro</a>
                                        <br/>
                                        <a href='album-13642-por-siempre-tu-y-yo.html?nc=1'>Por siempre tu y yo</a>
                                        <br/>
                                        <a href='album-466-a.html?nc=1'>A</a>
                                        <br/>
                                        <a href='album-19150-piron.html?nc=1'>Piron</a>
                                        <br/>
                                    </td>
                                </tr>
                            </table>
                            <br/>

                            <table class="main_tbl" cellspacing="0" style="width:160px">
                                <thead>
                                    <tr>
                                        <td>External Links</td>
                                    </tr>
                                </thead>
                                <tr>
                                    <td>
                                        <a href="http://www.mybestmatch.net/" target="_blank" title="A new, fresh dating site.">MyBestMatch.net</a>
                                        <br/>
                                        <a href="http://www.bianca-ryan.org/" target="_blank">Bianca Ryan fan site</a>
                                        <br/>
                                        <a href="http://video.croler.net/" title="Search for online videos - music, movie trailers, home videos" target="_blank">Croler Video Search</a>
                                        <br/>
                                        <script type="text/javascript">
                                        </script>
                                    </td>
                                </tr>
                            </table>
                        </div>
                    </td>
                    <td class="centerplane">
                        <form action="search" method="get">
                            <table id="search_form">
                                <tr>
                                    <td nowrap="nowrap">
                                        <input type="text" id="mq" name="mq" style="width:360px;" value="a million"/>
                                        <input type="submit" value="Search" style="font-weight:bold;"/>
                                        <input type="submit" name="btnI" value="I'm Feeling Lucky"/>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <table cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td nowrap="nowrap">
                                                    <input type="radio" name="si" id="sft" value="3"/>
                                                    <label for="sft">
                                                        <b>Fulltext</b>
                                                    </label>
                                                    <input type="radio" name="si" id="sar" value="1"/>
                                                    <label for="sar"> Artist</label>
                                                    <input type="radio" name="si" id="sti" value="2"/>
                                                    <label for="sti"> Title</label>
                                                    <input type="radio" name="si" id="sfl" value="0" checked="checked"/>
                                                    <label for="sfl"> Artist and title</label>
                                                    <br/>
                                                    <input type="radio" name="mm" id="mmall" value="0"/>
                                                    <label for="mmall"> All words</label>
                                                    <input type="radio" name="mm" id="mmany" value="1"/>
                                                    <label for="mmany"> Any word</label>
                                                    <input type="radio" name="mm" id="mmphrase" value="2" checked="checked"/>
                                                    <label for="mmphrase"> Exact phrase</label>
                                                </td>
                                                <td>&nbsp;</td>
                                                <td valign="top">Sort by:</td>
                                                <td>
                                                    <input type="radio" name="ob" id="obr" value="1" checked="checked"/>
                                                    <label for="obr"> Relevance</label>
                                                    <br/>
                                                    <input type="radio" name="ob" id="oba" value="2"/>
                                                    <label for="oba"> Rating</label>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </form>

                        <table id="thelist" cellspacing="0">
                            <tr>
                                <th>Artist(s)</th>
                                <th>Song</th>
                                <th width="20">Rating</th>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-31762-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-431-bosson.html'>Bosson</a>
                                </td>
                                <td class="ft">
                                    <a href="song-9278-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2611-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-4011-paint-your-wagon-soundtrack.html'>Paint Your Wagon Soundtrack</a>
                                </td>
                                <td class="ft">
                                    <a href="song-147768-a-million-miles-away-behind-the-door.html">A Million Miles Away Behind The Door</a>
                                </td>
                                <td align="right">1</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-3432-t-spoon.html'>T-Spoon</a>
                                </td>
                                <td class="ft">
                                    <a href="song-132065-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">1</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-2484-electric-light-orchestra.html'>Electric Light Orchestra</a>
                                </td>
                                <td class="ft">
                                    <a href="song-88720-power-of-a-million-lights.html">Power Of A Million Lights</a>
                                </td>
                                <td align="right">1</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-1440-kai.html'>KAI</a>
                                </td>
                                <td class="ft">
                                    <a href="song-52137-a-million-more.html">A Million More</a>
                                </td>
                                <td align="right">1</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-602-pet-shop-boys.html'>Pet Shop Boys</a>
                                </td>
                                <td class="ft">
                                    <a href="song-16624-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">1</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-3024-mr-big.html'>Mr. Big</a>
                                </td>
                                <td class="ft">
                                    <a href="song-246992-mr-never-in-a-million-years.html">Mr. Never In A Million Years</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-10569-flowing-tears.html'>Flowing Tears</a>
                                </td>
                                <td class="ft">
                                    <a href="song-239241-starfish-ride-for-a-million-dollar-handshake.html">Starfish Ride (For A Million Dollar Handshake)</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-9524-hannah-montana.html'>Hannah Montana</a>
                                </td>
                                <td class="ft">
                                    <a href="song-238912-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-1496-prince.html'>Prince</a>
                                </td>
                                <td class="ft">
                                    <a href="song-238007-a-million-days.html">A Million Days</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-9913-clan-of-xymox.html'>Clan Of Xymox</a>
                                </td>
                                <td class="ft">
                                    <a href="song-223458-a-million-things.html">A Million Things</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-9764-branigan-laura.html'>Branigan Laura</a>
                                </td>
                                <td class="ft">
                                    <a href="song-220971-never-in-a-million-years.html">Never In A Million Years</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-9695-bodyjar.html'>Bodyjar</a>
                                </td>
                                <td class="ft">
                                    <a href="song-219760-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-6547-ayreon.html'>Ayreon</a>
                                </td>
                                <td class="ft">
                                    <a href="song-217756-dawn-of-a-million-souls.html">Dawn Of A Million Souls</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-803-ok-go.html'>Ok Go</a>
                                </td>
                                <td class="ft">
                                    <a href="song-211898-a-million-ways.html">A Million Ways</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-9352-charlie-landsborough.html'>Charlie Landsborough</a>
                                </td>
                                <td class="ft">
                                    <a href="song-209131-a-million-ways-to-fall.html">A Million Ways To Fall</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-156-helloween.html'>Helloween</a>
                                </td>
                                <td class="ft">
                                    <a href="song-208245-a-million-to-one.html">A million to One</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-8575-rihanna.html'>Rihanna</a>
                                </td>
                                <td class="ft">
                                    <a href="song-208029-a-million-miles-away.html">A Million Miles Away</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-9101-mercyme.html'>Mercyme</a>
                                </td>
                                <td class="ft">
                                    <a href="song-199874-a-million-miles-away.html">A Million Miles Away</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-9090-lostprophets.html'>Lostprophets</a>
                                </td>
                                <td class="ft">
                                    <a href="song-199509-a-million-miles.html">A Million Miles</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-7285-gotthard.html'>Gotthard</a>
                                </td>
                                <td class="ft">
                                    <a href="song-176853-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-7075-eddie-cochran.html'>Eddie Cochran</a>
                                </td>
                                <td class="ft">
                                    <a href="song-174863-a-million-teardrops.html">A Million Teardrops</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-6431-alexz-johnson.html'>Alexz Johnson</a>
                                </td>
                                <td class="ft">
                                    <a href="song-168138-one-in-a-million-world.html">One In A Million World</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-3828-funny-lady-soundtrack.html'>Funny Lady Soundtrack</a>
                                </td>
                                <td class="ft">
                                    <a href="song-145713-i-found-a-million-dollar-baby.html">I FOUND A MILLION DOLLAR BABY</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-3648-xymox.html'>Xymox</a>
                                </td>
                                <td class="ft">
                                    <a href="song-143148-a-million-things.html">A Million Things</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-3642-wolfsheim.html'>Wolfsheim</a>
                                </td>
                                <td class="ft">
                                    <a href="song-143001-a-million-miles.html">A million miles</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-3521-the-runaways.html'>The Runaways</a>
                                </td>
                                <td class="ft">
                                    <a href="song-136628-i-m-a-million.html">I'm A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-3442-tara-maclean.html'>Tara MacLean</a>
                                </td>
                                <td class="ft">
                                    <a href="song-132369-a-million-miles-to-the-city.html">A Million Miles To The City</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                        </table>
                        <script type="text/javascript">
                        InitDataView("thelist", "#F7F7FF", "#FFFFFF");
                        </script>
                        <br/>
                        <div align="center" style="width:596px;">
                            <input type="button" value=" &lt;&lt; " class="button" disabled="disabled" onclick="document.location.href='search?mq=a+million&amp;mm=2&amp;si=0&amp;from=0'" style="cursor:default"/>
                            <b>1</b>
                            <font color="black"> | </font>
                            <a href="search?mq=a+million&amp;mm=2&amp;si=0&amp;from=30" onfocus="this.blur()">2</a>
                            <font color="black"> | </font>
                            <a href="search?mq=a+million&amp;mm=2&amp;si=0&amp;from=60" onfocus="this.blur()">3</a>
                            <font color="black"> | </font>
                            <a href="search?mq=a+million&amp;mm=2&amp;si=0&amp;from=90" onfocus="this.blur()">4</a>
                            <input type="button" value=" &gt;&gt; " class="button" onclick="document.location.href='search?mq=a+million&amp;mm=2&amp;si=0&amp;from=30'" style="cursor:hand"/>
                        </div>
                        <script type="text/javascript">
                        document.getElementById('mq').focus();
                        </script>
                    </td>
                </tr>
            </table>
            <table width="100%" cellspacing="0" cellpadding="2">
                <tr>
                    <td align="center" style="border-top:2px dashed #E0E0E0;font-family:verdana, arial;font-size:12px;">
                    All lyrics are property and copyright of their owners.
                    </td>
                </tr>
            </table>
        </div>
    </center>

    <script>
    (function(i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] || function() {
            (i[r].q = i[r].q || []).push(arguments)
        },
        i[r].l = 1 * new Date();
        a = s.createElement(o),
        m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
    })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

    ga('create', 'UA-319914-9', 'auto');
    ga('send', 'pageview');
    </script>
</body>
</html>


"""

p2 = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <title>MLDb, The Music Lyrics Database - Advanced search</title>
    <meta name="Author" content="Nikolay Pelov, NickSoft"/>
    <meta name="Description" content="MLDb - Advanced search. Searching for &amp;quot;a million&amp;quot;"/>
    <meta name="Keywords" content="music,song,lyrics,mldb"/>
    <meta name="robots" content="index,follow"/>
    <meta name="revisit-after" content="7 days"/>
    <meta name="title" content="MLDb, The Music Lyrics Database - Advanced search"/>
    <meta name="distribution" content="Global"/>
    <meta name="rating" content="general"/>
    <link href="style.css" media="all" type="text/css" rel="stylesheet"/>
    <link href="/favicon.ico" rel="shortcut icon"/>
    <link rel="search" type="application/opensearchdescription+xml" href="http://www.mldb.org/opensearch.xml" title="MLDb music lyrics search"/>
    <!-- music song lyrics database begins -->
    <!-- music song lyrics database navigation links -->
    <link rel="MLDb - Home" title="Music lyrics" href="http://www.mldb.org/"/>
    <link rel="section" title="Music lyrics Search" href="http://www.mldb.org/search"/>
    <link rel="section" title="Top 40 Music Lyrics" href="http://www.mldb.org/top40.html"/>
    <link rel="section" title="Latest Music Lyrics" href="http://www.mldb.org/new-lyrics.html"/>
    <link rel="section" title="Submit music lyrics to database" href="http://www.mldb.org/submit.html"/>
    <link rel="contents" title="Extras: toolbar buttons, firefox search box" href="http://www.mldb.org/extras.html"/>
    <style type="text/css">
        <!--
        .dnone{
          display:none;
        }
        -->
        
    </style>
    <!-- International portal to music lyrics. Sorted lyrics by artist name. Clean and easy-to-use site with over 220,000 lyrics -->
    <!-- Top 40 lyrics chart. Comprehensive music lyrics search engine. Fulltext lyrics search. Search by artist, title, both of them or song lyrics -->
    <!-- <link rel="prefetch" href="http://"> -->
    <script type="text/javascript" src="js/main.js?v=3"></script>
    <script type="text/javascript" src="/js/ST.min.js?v=2"></script>
</head>
<body style="margin: 0px; padding: 0px;">
    <center>
        <div id="container">
            <table id="toptbl" align="center" cellspacing="0">
                <tr>
                    <td>
                        <!--<img src='img/headerbg.png' id="topimg" />-->
                        <div id="topadframe">
                            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9307576326974516" crossorigin="anonymous"></script>
                            <!-- MLDb top 468x60 -->
                            <ins class="adsbygoogle" style="display:inline-block;width:468px;height:60px" data-ad-client="ca-pub-9307576326974516" data-ad-slot="9720604683"></ins>
                            <script>
                            (adsbygoogle = window.adsbygoogle || []).push({});
                            </script>
                        </div>
                        <div id="toplinks" style="width:200px;position:absolute;">
                            <a href="/advertise.html" style="color:orange">Advertise</a>
                            <a href='/contact.html'>contact us</a>
                        </div>
                        <div style="height:80px"></div>
                        <div id="nav">
                            <div style="height:6px">
                                <img alt="" src="img/spacer.gif" width="1" height="6"/>
                            </div>
                            <div id="tabs" align="left">
                                <ul>
                                    <li>
                                        <a href="/" title="Music Lyrics Database Homepage">home</a>
                                    </li>
                                    <li>
                                        <a href="/aza-A.html" title="Complete artist list">artists</a>
                                    </li>
                                    <li>
                                        <a href="/azl-A.html" title="Complete album list">albums</a>
                                    </li>
                                    <li>
                                        <a href="/search?v=3" title="Search for song lyrics, detailed search" class="active">search</a>
                                    </li>
                                    <li>
                                        <a href="/top40.html" title="Top Chart of Music Lyrics Database">top 40</a>
                                    </li>
                                    <li>
                                        <a href="/new-lyrics.html" title="New lyrics">new</a>
                                    </li>
                                    <li>
                                        <a href="/submit.html" title="Submit new lyrics - help to make the world biggest music lyrics collection" style="color:#FFE090;">submit</a>
                                    </li>
                                    <li>
                                        <a href="/extras.html" title="Browser toolbars, buttons, search boxes." style="border-right: 1px solid rgb(119, 119, 119);">extras</a>
                                    </li>
                                </ul>
                            </div>
                            <div class="underline">
                                <img src="img/spacer.gif" alt="Main menu" height="2" width="1"/>
                            </div>
                            <!--  <div style="border-left: 1px solid rgb(119, 119, 119); float: left; height: 1px;"></div>-->
                            <div id="ajaxNav">
                                <div id="az" class="slip">
                                    <ul>
                                        <li>
                                            <a href="aza-0.html">#</a>
                                            <a href="aza-A.html">A</a>
                                            <a href="aza-B.html">B</a>
                                            <a href="aza-C.html">C</a>
                                            <a href="aza-D.html">D</a>
                                            <a href="aza-E.html">E</a>
                                            <a href="aza-F.html">F</a>
                                            <a href="aza-G.html">G</a>
                                            <a href="aza-H.html">H</a>
                                            <a href="aza-I.html">I</a>
                                            <a href="aza-J.html">J</a>
                                            <a href="aza-K.html">K</a>
                                            <a href="aza-L.html">L</a>
                                            <a href="aza-M.html">M</a>
                                            <a href="aza-N.html">N</a>
                                            <a href="aza-O.html">O</a>
                                            <a href="aza-P.html">P</a>
                                            <a href="aza-Q.html">Q</a>
                                            <a href="aza-R.html">R</a>
                                            <a href="aza-S.html">S</a>
                                            <a href="aza-T.html">T</a>
                                            <a href="aza-U.html">U</a>
                                            <a href="aza-V.html">V</a>
                                            <a href="aza-W.html">W</a>
                                            <a href="aza-X.html">X</a>
                                            <a href="aza-Y.html">Y</a>
                                            <a href="aza-Z.html">Z</a>
                                            <a href="aza-_.html">*</a>
                                        </li>

                                    </ul>
                                </div>
                            </div>
                        </div>
                    </td>
                </tr>
            </table>
            <table id="centertbl" align="center" cellspacing="0">
                <tr>
                    <td colspan="2" class="center">
                        <!-- page IS safe center -->
                        <div style="width:728px;height:90px;margin:auto">
                            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9307576326974516" crossorigin="anonymous"></script>
                            <!-- MLDb below top nav 728x90 -->
                            <ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-9307576326974516" data-ad-slot="5179889214"></ins>
                            <script>
                            (adsbygoogle = window.adsbygoogle || []).push({});
                            </script>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td class="leftplane">
                        <div style="width:160px">
                            <!-- Left Nav -->
                            <script type="text/javascript">
                            searchBox();
                            </script>
                            <br/>
                            <br/>
                            <script type="text/javascript">
                            drawStats(236679, 24057, 11223, 183);
                            </script>
                            <br/>
                            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9307576326974516" crossorigin="anonymous"></script>
                            <!-- MLDB Left Sidebar 160x600 -->
                            <ins class="adsbygoogle" style="display:inline-block;width:160px;height:600px" data-ad-client="ca-pub-9307576326974516" data-ad-slot="7838877680"></ins>
                            <script>
                            (adsbygoogle = window.adsbygoogle || []).push({});
                            </script>
                            <br/>
                            <br/>
                            <table class="main_tbl" cellspacing="0" style="width:160px">
                                <thead>
                                    <tr>
                                        <td>Top artists</td>
                                    </tr>
                                </thead>
                                <tr>
                                    <td>
                                        <a href='artist-3796-a-funny-thing-happened-on-the-way-to-the-forum-soundtrack.html?nc=1'>A Funny Thing Happened on the Way to the Forum Soundtrack</a>
                                        <br/>
                                        <a href='artist-25-metallica.html?nc=1'>Metallica</a>
                                        <br/>
                                        <a href='artist-278-a.html?nc=1'>A</a>
                                        <br/>
                                        <a href='artist-3795-a-charlie-brown-christmas-soundtrack.html?nc=1'>A Charlie Brown Christmas Soundtrack</a>
                                        <br/>
                                        <a href='artist-3807-fame-soundtrack.html?nc=1'>Fame Soundtrack</a>
                                        <br/>
                                    </td>
                                </tr>
                            </table>
                            <br/>
                            <table class="main_tbl" cellspacing="0" style="width:160px">
                                <thead>
                                    <tr>
                                        <td>Top albums</td>
                                    </tr>
                                </thead>
                                <tr>
                                    <td>
                                        <a href='album-12771-a-funny-thing-happened-on-the-way-to-the-forum-soundtrack.html?nc=1'>A Funny Thing Happened on the Way to the Forum Soundtrack</a>
                                        <br/>
                                        <a href='album-21665-a-arte-de-leila-pinheiro.html?nc=1'>A Arte de Leila Pinheiro</a>
                                        <br/>
                                        <a href='album-13642-por-siempre-tu-y-yo.html?nc=1'>Por siempre tu y yo</a>
                                        <br/>
                                        <a href='album-466-a.html?nc=1'>A</a>
                                        <br/>
                                        <a href='album-19150-piron.html?nc=1'>Piron</a>
                                        <br/>
                                    </td>
                                </tr>
                            </table>
                            <br/>

                            <table class="main_tbl" cellspacing="0" style="width:160px">
                                <thead>
                                    <tr>
                                        <td>External Links</td>
                                    </tr>
                                </thead>
                                <tr>
                                    <td>
                                        <a href="http://www.mybestmatch.net/" target="_blank" title="A new, fresh dating site.">MyBestMatch.net</a>
                                        <br/>
                                        <a href="http://www.bianca-ryan.org/" target="_blank">Bianca Ryan fan site</a>
                                        <br/>
                                        <a href="http://video.croler.net/" title="Search for online videos - music, movie trailers, home videos" target="_blank">Croler Video Search</a>
                                        <br/>
                                        <script type="text/javascript">
                                        </script>
                                    </td>
                                </tr>
                            </table>
                        </div>
                    </td>
                    <td class="centerplane">
                        <form action="search" method="get">
                            <table id="search_form">
                                <tr>
                                    <td nowrap="nowrap">
                                        <input type="text" id="mq" name="mq" style="width:360px;" value="a million"/>
                                        <input type="submit" value="Search" style="font-weight:bold;"/>
                                        <input type="submit" name="btnI" value="I'm Feeling Lucky"/>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <table cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td nowrap="nowrap">
                                                    <input type="radio" name="si" id="sft" value="3"/>
                                                    <label for="sft">
                                                        <b>Fulltext</b>
                                                    </label>
                                                    <input type="radio" name="si" id="sar" value="1"/>
                                                    <label for="sar"> Artist</label>
                                                    <input type="radio" name="si" id="sti" value="2"/>
                                                    <label for="sti"> Title</label>
                                                    <input type="radio" name="si" id="sfl" value="0" checked="checked"/>
                                                    <label for="sfl"> Artist and title</label>
                                                    <br/>
                                                    <input type="radio" name="mm" id="mmall" value="0"/>
                                                    <label for="mmall"> All words</label>
                                                    <input type="radio" name="mm" id="mmany" value="1"/>
                                                    <label for="mmany"> Any word</label>
                                                    <input type="radio" name="mm" id="mmphrase" value="2" checked="checked"/>
                                                    <label for="mmphrase"> Exact phrase</label>
                                                </td>
                                                <td>&nbsp;</td>
                                                <td valign="top">Sort by:</td>
                                                <td>
                                                    <input type="radio" name="ob" id="obr" value="1" checked="checked"/>
                                                    <label for="obr"> Relevance</label>
                                                    <br/>
                                                    <input type="radio" name="ob" id="oba" value="2"/>
                                                    <label for="oba"> Rating</label>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </form>

                        <table id="thelist" cellspacing="0">
                            <tr>
                                <th>Artist(s)</th>
                                <th>Song</th>
                                <th width="20">Rating</th>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-3396-steve-miller.html'>Steve Miller</a>
                                </td>
                                <td class="ft">
                                    <a href="song-130631-one-in-a-million.html">One in a Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-3306-selena.html'>Selena</a>
                                </td>
                                <td class="ft">
                                    <a href="song-126855-a-million-to-one.html">A Million To One</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-3306-selena.html'>Selena</a>
                                </td>
                                <td class="ft">
                                    <a href="song-126724-a-million-to-one.html">A Million To One</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-3284-samantha-fox.html'>Samantha Fox</a>
                                </td>
                                <td class="ft">
                                    <a href="song-125895-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-3249-roger-miller.html'>Roger Miller</a>
                                </td>
                                <td class="ft">
                                    <a href="song-124541-a-million-years-or-so.html">A Million Years Or So</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-3171-picture-house.html'>Picture House</a>
                                </td>
                                <td class="ft">
                                    <a href="song-120277-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-3171-picture-house.html'>Picture House</a>
                                </td>
                                <td class="ft">
                                    <a href="song-120267-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-3094-nylons.html'>Nylons</a>
                                </td>
                                <td class="ft">
                                    <a href="song-116611-a-million-ways.html">A Million Ways</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-3065-new-edition.html'>New Edition</a>
                                </td>
                                <td class="ft">
                                    <a href="song-115664-a-million-to-one.html">A Million To One</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-2846-lynch-mob.html'>Lynch Mob</a>
                                </td>
                                <td class="ft">
                                    <a href="song-107231-for-a-million-years.html">For A Million Years</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-2841-level-42.html'>Level 42</a>
                                </td>
                                <td class="ft">
                                    <a href="song-107106-one-in-a-million.html">One in a million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-2597-gilbert-o-sullivan.html'>Gilbert O'Sullivan</a>
                                </td>
                                <td class="ft">
                                    <a href="song-95111-not-in-a-million-years.html">Not in a Million Years</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-2373-dean-friedman.html'>Dean Friedman</a>
                                </td>
                                <td class="ft">
                                    <a href="song-83626-maybe-in-a-million-years.html">Maybe in a Million Years</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-2351-david-byrne.html'>David Byrne</a>
                                </td>
                                <td class="ft">
                                    <a href="song-82714-a-million-miles-away.html">A Million Miles Away</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-2287-conception.html'>Conception</a>
                                </td>
                                <td class="ft">
                                    <a href="song-80886-a-million-gods.html">A Million Gods</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-2273-christine-mcvie.html'>Christine McVie</a>
                                </td>
                                <td class="ft">
                                    <a href="song-80273-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-2217-bryan-white.html'>Bryan White</a>
                                </td>
                                <td class="ft">
                                    <a href="song-77685-two-in-a-million.html">Two In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-2173-blake-babies.html'>Blake Babies</a>
                                </td>
                                <td class="ft">
                                    <a href="song-75697-a-million-years.html">A million years</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-2159-billy-rankin.html'>Billy Rankin</a>
                                </td>
                                <td class="ft">
                                    <a href="song-75377-never-in-a-million-years.html">Never in a Million Years</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-2083-asia.html'>Asia</a>
                                </td>
                                <td class="ft">
                                    <a href="song-71816-never-in-a-million-years.html">Never In A Million Years</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-2026-america.html'>America</a>
                                </td>
                                <td class="ft">
                                    <a href="song-69991-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-2020-alphaville.html'>Alphaville</a>
                                </td>
                                <td class="ft">
                                    <a href="song-69773-for-a-million.html">for a million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-60-scorpions.html'>Scorpions</a>
                                </td>
                                <td class="ft">
                                    <a href="song-59177-they-need-a-million.html">They Need A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-60-scorpions.html'>Scorpions</a>
                                </td>
                                <td class="ft">
                                    <a href="song-58912-a-moment-in-a-million-years.html">A Moment In A Million Years</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-814-outkast.html'>Outkast</a>
                                </td>
                                <td class="ft">
                                    <a href="song-55575-land-of-a-million-drums.html">Land Of A Million Drums</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-1474-modern-talking.html'>Modern Talking</a>
                                </td>
                                <td class="ft">
                                    <a href="song-54533-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-1474-modern-talking.html'>Modern Talking</a>
                                </td>
                                <td class="ft">
                                    <a href="song-54532-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-1442-keith-sweat.html'>Keith Sweat</a>
                                </td>
                                <td class="ft">
                                    <a href="song-52342-i-ll-trade-a-million-dollars.html">I'll Trade (A Million Dollars)</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-869-jay-z.html'>Jay-Z</a>
                                </td>
                                <td class="ft">
                                    <a href="song-51374-a-million-and-1-questions-extended.html">A Million And 1 Questions (Extended)</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-41041-one-in-a-million-remix.html">One In A Million (Remix)</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                        </table>
                        <script type="text/javascript">
                        InitDataView("thelist", "#F7F7FF", "#FFFFFF");
                        </script>
                        <br/>
                        <div align="center" style="width:596px;">
                            <input type="button" value=" &lt;&lt; " class="button" onclick="document.location.href='search?mq=a+million&amp;mm=2&amp;si=0&amp;from=0'" style="cursor:hand"/>
                            <a href="search?mq=a+million&amp;mm=2&amp;si=0&amp;from=0" onfocus="this.blur()">1</a>
                            <font color="black"> | </font>
                            <b>2</b>
                            <font color="black"> | </font>
                            <a href="search?mq=a+million&amp;mm=2&amp;si=0&amp;from=60" onfocus="this.blur()">3</a>
                            <font color="black"> | </font>
                            <a href="search?mq=a+million&amp;mm=2&amp;si=0&amp;from=90" onfocus="this.blur()">4</a>
                            <input type="button" value=" &gt;&gt; " class="button" onclick="document.location.href='search?mq=a+million&amp;mm=2&amp;si=0&amp;from=60'" style="cursor:hand"/>
                        </div>
                        <script type="text/javascript">
                        document.getElementById('mq').focus();
                        </script>
                    </td>
                </tr>
            </table>
            <table width="100%" cellspacing="0" cellpadding="2">
                <tr>
                    <td align="center" style="border-top:2px dashed #E0E0E0;font-family:verdana, arial;font-size:12px;">
                    All lyrics are property and copyright of their owners.
                    </td>
                </tr>
            </table>
        </div>
    </center>

    <script>
    (function(i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] || function() {
            (i[r].q = i[r].q || []).push(arguments)
        },
        i[r].l = 1 * new Date();
        a = s.createElement(o),
        m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
    })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

    ga('create', 'UA-319914-9', 'auto');
    ga('send', 'pageview');
    </script>
</body>
</html>


"""

p3 = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <title>MLDb, The Music Lyrics Database - Advanced search</title>
    <meta name="Author" content="Nikolay Pelov, NickSoft"/>
    <meta name="Description" content="MLDb - Advanced search. Searching for &amp;quot;a million&amp;quot;"/>
    <meta name="Keywords" content="music,song,lyrics,mldb"/>
    <meta name="robots" content="index,follow"/>
    <meta name="revisit-after" content="7 days"/>
    <meta name="title" content="MLDb, The Music Lyrics Database - Advanced search"/>
    <meta name="distribution" content="Global"/>
    <meta name="rating" content="general"/>
    <link href="style.css" media="all" type="text/css" rel="stylesheet"/>
    <link href="/favicon.ico" rel="shortcut icon"/>
    <link rel="search" type="application/opensearchdescription+xml" href="http://www.mldb.org/opensearch.xml" title="MLDb music lyrics search"/>
    <!-- music song lyrics database begins -->
    <!-- music song lyrics database navigation links -->
    <link rel="MLDb - Home" title="Music lyrics" href="http://www.mldb.org/"/>
    <link rel="section" title="Music lyrics Search" href="http://www.mldb.org/search"/>
    <link rel="section" title="Top 40 Music Lyrics" href="http://www.mldb.org/top40.html"/>
    <link rel="section" title="Latest Music Lyrics" href="http://www.mldb.org/new-lyrics.html"/>
    <link rel="section" title="Submit music lyrics to database" href="http://www.mldb.org/submit.html"/>
    <link rel="contents" title="Extras: toolbar buttons, firefox search box" href="http://www.mldb.org/extras.html"/>
    <style type="text/css">
        <!--
        .dnone{
          display:none;
        }
        -->
        
    </style>
    <!-- International portal to music lyrics. Sorted lyrics by artist name. Clean and easy-to-use site with over 220,000 lyrics -->
    <!-- Top 40 lyrics chart. Comprehensive music lyrics search engine. Fulltext lyrics search. Search by artist, title, both of them or song lyrics -->
    <!-- <link rel="prefetch" href="http://"> -->
    <script type="text/javascript" src="js/main.js?v=3"></script>
    <script type="text/javascript" src="/js/ST.min.js?v=2"></script>
</head>
<body style="margin: 0px; padding: 0px;">
    <center>
        <div id="container">
            <table id="toptbl" align="center" cellspacing="0">
                <tr>
                    <td>
                        <!--<img src='img/headerbg.png' id="topimg" />-->
                        <div id="topadframe">
                            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9307576326974516" crossorigin="anonymous"></script>
                            <!-- MLDb top 468x60 -->
                            <ins class="adsbygoogle" style="display:inline-block;width:468px;height:60px" data-ad-client="ca-pub-9307576326974516" data-ad-slot="9720604683"></ins>
                            <script>
                            (adsbygoogle = window.adsbygoogle || []).push({});
                            </script>
                        </div>
                        <div id="toplinks" style="width:200px;position:absolute;">
                            <a href="/advertise.html" style="color:orange">Advertise</a>
                            <a href='/contact.html'>contact us</a>
                        </div>
                        <div style="height:80px"></div>
                        <div id="nav">
                            <div style="height:6px">
                                <img alt="" src="img/spacer.gif" width="1" height="6"/>
                            </div>
                            <div id="tabs" align="left">
                                <ul>
                                    <li>
                                        <a href="/" title="Music Lyrics Database Homepage">home</a>
                                    </li>
                                    <li>
                                        <a href="/aza-A.html" title="Complete artist list">artists</a>
                                    </li>
                                    <li>
                                        <a href="/azl-A.html" title="Complete album list">albums</a>
                                    </li>
                                    <li>
                                        <a href="/search?v=3" title="Search for song lyrics, detailed search" class="active">search</a>
                                    </li>
                                    <li>
                                        <a href="/top40.html" title="Top Chart of Music Lyrics Database">top 40</a>
                                    </li>
                                    <li>
                                        <a href="/new-lyrics.html" title="New lyrics">new</a>
                                    </li>
                                    <li>
                                        <a href="/submit.html" title="Submit new lyrics - help to make the world biggest music lyrics collection" style="color:#FFE090;">submit</a>
                                    </li>
                                    <li>
                                        <a href="/extras.html" title="Browser toolbars, buttons, search boxes." style="border-right: 1px solid rgb(119, 119, 119);">extras</a>
                                    </li>
                                </ul>
                            </div>
                            <div class="underline">
                                <img src="img/spacer.gif" alt="Main menu" height="2" width="1"/>
                            </div>
                            <!--  <div style="border-left: 1px solid rgb(119, 119, 119); float: left; height: 1px;"></div>-->
                            <div id="ajaxNav">
                                <div id="az" class="slip">
                                    <ul>
                                        <li>
                                            <a href="aza-0.html">#</a>
                                            <a href="aza-A.html">A</a>
                                            <a href="aza-B.html">B</a>
                                            <a href="aza-C.html">C</a>
                                            <a href="aza-D.html">D</a>
                                            <a href="aza-E.html">E</a>
                                            <a href="aza-F.html">F</a>
                                            <a href="aza-G.html">G</a>
                                            <a href="aza-H.html">H</a>
                                            <a href="aza-I.html">I</a>
                                            <a href="aza-J.html">J</a>
                                            <a href="aza-K.html">K</a>
                                            <a href="aza-L.html">L</a>
                                            <a href="aza-M.html">M</a>
                                            <a href="aza-N.html">N</a>
                                            <a href="aza-O.html">O</a>
                                            <a href="aza-P.html">P</a>
                                            <a href="aza-Q.html">Q</a>
                                            <a href="aza-R.html">R</a>
                                            <a href="aza-S.html">S</a>
                                            <a href="aza-T.html">T</a>
                                            <a href="aza-U.html">U</a>
                                            <a href="aza-V.html">V</a>
                                            <a href="aza-W.html">W</a>
                                            <a href="aza-X.html">X</a>
                                            <a href="aza-Y.html">Y</a>
                                            <a href="aza-Z.html">Z</a>
                                            <a href="aza-_.html">*</a>
                                        </li>

                                    </ul>
                                </div>
                            </div>
                        </div>
                    </td>
                </tr>
            </table>
            <table id="centertbl" align="center" cellspacing="0">
                <tr>
                    <td colspan="2" class="center">
                        <!-- page IS safe center -->
                        <div style="width:728px;height:90px;margin:auto">
                            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9307576326974516" crossorigin="anonymous"></script>
                            <!-- MLDb below top nav 728x90 -->
                            <ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-9307576326974516" data-ad-slot="5179889214"></ins>
                            <script>
                            (adsbygoogle = window.adsbygoogle || []).push({});
                            </script>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td class="leftplane">
                        <div style="width:160px">
                            <!-- Left Nav -->
                            <script type="text/javascript">
                            searchBox();
                            </script>
                            <br/>
                            <br/>
                            <script type="text/javascript">
                            drawStats(236679, 24057, 11223, 183);
                            </script>
                            <br/>
                            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9307576326974516" crossorigin="anonymous"></script>
                            <!-- MLDB Left Sidebar 160x600 -->
                            <ins class="adsbygoogle" style="display:inline-block;width:160px;height:600px" data-ad-client="ca-pub-9307576326974516" data-ad-slot="7838877680"></ins>
                            <script>
                            (adsbygoogle = window.adsbygoogle || []).push({});
                            </script>
                            <br/>
                            <br/>
                            <table class="main_tbl" cellspacing="0" style="width:160px">
                                <thead>
                                    <tr>
                                        <td>Top artists</td>
                                    </tr>
                                </thead>
                                <tr>
                                    <td>
                                        <a href='artist-3796-a-funny-thing-happened-on-the-way-to-the-forum-soundtrack.html?nc=1'>A Funny Thing Happened on the Way to the Forum Soundtrack</a>
                                        <br/>
                                        <a href='artist-25-metallica.html?nc=1'>Metallica</a>
                                        <br/>
                                        <a href='artist-278-a.html?nc=1'>A</a>
                                        <br/>
                                        <a href='artist-3795-a-charlie-brown-christmas-soundtrack.html?nc=1'>A Charlie Brown Christmas Soundtrack</a>
                                        <br/>
                                        <a href='artist-3807-fame-soundtrack.html?nc=1'>Fame Soundtrack</a>
                                        <br/>
                                    </td>
                                </tr>
                            </table>
                            <br/>
                            <table class="main_tbl" cellspacing="0" style="width:160px">
                                <thead>
                                    <tr>
                                        <td>Top albums</td>
                                    </tr>
                                </thead>
                                <tr>
                                    <td>
                                        <a href='album-12771-a-funny-thing-happened-on-the-way-to-the-forum-soundtrack.html?nc=1'>A Funny Thing Happened on the Way to the Forum Soundtrack</a>
                                        <br/>
                                        <a href='album-21665-a-arte-de-leila-pinheiro.html?nc=1'>A Arte de Leila Pinheiro</a>
                                        <br/>
                                        <a href='album-13642-por-siempre-tu-y-yo.html?nc=1'>Por siempre tu y yo</a>
                                        <br/>
                                        <a href='album-466-a.html?nc=1'>A</a>
                                        <br/>
                                        <a href='album-19150-piron.html?nc=1'>Piron</a>
                                        <br/>
                                    </td>
                                </tr>
                            </table>
                            <br/>

                            <table class="main_tbl" cellspacing="0" style="width:160px">
                                <thead>
                                    <tr>
                                        <td>External Links</td>
                                    </tr>
                                </thead>
                                <tr>
                                    <td>
                                        <a href="http://www.mybestmatch.net/" target="_blank" title="A new, fresh dating site.">MyBestMatch.net</a>
                                        <br/>
                                        <a href="http://www.bianca-ryan.org/" target="_blank">Bianca Ryan fan site</a>
                                        <br/>
                                        <a href="http://video.croler.net/" title="Search for online videos - music, movie trailers, home videos" target="_blank">Croler Video Search</a>
                                        <br/>
                                        <script type="text/javascript">
                                        </script>
                                    </td>
                                </tr>
                            </table>
                        </div>
                    </td>
                    <td class="centerplane">
                        <form action="search" method="get">
                            <table id="search_form">
                                <tr>
                                    <td nowrap="nowrap">
                                        <input type="text" id="mq" name="mq" style="width:360px;" value="a million"/>
                                        <input type="submit" value="Search" style="font-weight:bold;"/>
                                        <input type="submit" name="btnI" value="I'm Feeling Lucky"/>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <table cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td nowrap="nowrap">
                                                    <input type="radio" name="si" id="sft" value="3"/>
                                                    <label for="sft">
                                                        <b>Fulltext</b>
                                                    </label>
                                                    <input type="radio" name="si" id="sar" value="1"/>
                                                    <label for="sar"> Artist</label>
                                                    <input type="radio" name="si" id="sti" value="2"/>
                                                    <label for="sti"> Title</label>
                                                    <input type="radio" name="si" id="sfl" value="0" checked="checked"/>
                                                    <label for="sfl"> Artist and title</label>
                                                    <br/>
                                                    <input type="radio" name="mm" id="mmall" value="0"/>
                                                    <label for="mmall"> All words</label>
                                                    <input type="radio" name="mm" id="mmany" value="1"/>
                                                    <label for="mmany"> Any word</label>
                                                    <input type="radio" name="mm" id="mmphrase" value="2" checked="checked"/>
                                                    <label for="mmphrase"> Exact phrase</label>
                                                </td>
                                                <td>&nbsp;</td>
                                                <td valign="top">Sort by:</td>
                                                <td>
                                                    <input type="radio" name="ob" id="obr" value="1" checked="checked"/>
                                                    <label for="obr"> Relevance</label>
                                                    <br/>
                                                    <input type="radio" name="ob" id="oba" value="2"/>
                                                    <label for="oba"> Rating</label>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </form>

                        <table id="thelist" cellspacing="0">
                            <tr>
                                <th>Artist(s)</th>
                                <th>Song</th>
                                <th width="20">Rating</th>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-1279-jim-boyd.html'>Jim Boyd</a>
                                </td>
                                <td class="ft">
                                    <a href="song-40639-a-million-miles-away.html">A Million Miles Away</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-739-redman.html'>Redman</a>
                                </td>
                                <td class="ft">
                                    <a href="song-37805-a-million-and-1-buddah-spots.html">A Million And 1 Buddah Spots</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-869-jay-z.html'>Jay-Z</a>
                                </td>
                                <td class="ft">
                                    <a href="song-35647-intro-a-million-and-one-questions-rhyme-no-mor.html">Intro  A Million And One Questions  Rhyme No Mor</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-923-guns-n-roses.html'>Guns' N' Roses</a>
                                </td>
                                <td class="ft">
                                    <a href="song-28958-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-869-jay-z.html'>Jay-Z</a>
                                </td>
                                <td class="ft">
                                    <a href="song-26781-a-million-and-1-questions-extended.html">A Million and 1 Questions (Extended)</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-869-jay-z.html'>Jay-Z</a>
                                </td>
                                <td class="ft">
                                    <a href="song-26660-intro-a-million-and-one-questions-rhyme-no-mor.html">Intro / A Million And One Questions / Rhyme No Mor</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-833-moody-blues.html'>Moody Blues</a>
                                </td>
                                <td class="ft">
                                    <a href="song-25114-i-never-thought-i-d-live-to-be-a-million.html">I Never Thought I'd Live To Be A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-814-outkast.html'>Outkast</a>
                                </td>
                                <td class="ft">
                                    <a href="song-24491-land-of-a-million-drums.html">Land Of A Million Drums</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-706-s-club-7.html'>S Club 7</a>
                                </td>
                                <td class="ft">
                                    <a href="song-20783-two-in-a-million.html">Two In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-683-juvenile.html'>Juvenile</a>
                                </td>
                                <td class="ft">
                                    <a href="song-20137-a-million-and-one-things.html">A Million and One Things</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-669-take-that.html'>Take That</a>
                                </td>
                                <td class="ft">
                                    <a href="song-19653-a-million-love-songs.html">A Million Love Songs</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-189-sugababes.html'>Sugababes</a>
                                </td>
                                <td class="ft">
                                    <a href="song-19088-more-than-a-million-miles.html">More Than A Million Miles</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-543-lenny-kravitz.html'>Lenny Kravitz</a>
                                </td>
                                <td class="ft">
                                    <a href="song-14078-a-million-miles-away.html">A Million Miles Away</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-524-kasey-chambers.html'>Kasey Chambers</a>
                                </td>
                                <td class="ft">
                                    <a href="song-13409-a-million-tears.html">A Million Tears</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-397-big-tymers.html'>Big Tymers</a>
                                </td>
                                <td class="ft">
                                    <a href="song-7781-try-n-2-make-a-million.html">Try'n 2 Make A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-312-toto.html'>Toto</a>
                                </td>
                                <td class="ft">
                                    <a href="song-4299-a-million-miles-away.html">A Million Miles Away</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2643-one-in-a-million.html">One In A Million</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-431-bosson.html'>Bosson</a>
                                </td>
                                <td class="ft">
                                    <a href="song-9287-hole-in-my-heart.html">Hole In My Heart</a>
                                </td>
                                <td align="right">1</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-431-bosson.html'>Bosson</a>
                                </td>
                                <td class="ft">
                                    <a href="song-44594-we-will-meet-again.html">We Will Meet Again</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-41181-givin-you-more.html">Givin' You More</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-41180-i-gotcha-back.html">I Gotcha' Back</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-31764-never-comin-back.html">Never Comin Back</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-31763-never-giving-up.html">Never Giving Up</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-31761-beats-4-da-streets-intro.html">Beats 4 Da Streets (Intro)</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-31760-everything-s-gonna-be-alright.html">Everything's Gonna Be Alright</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-431-bosson.html'>Bosson</a>
                                </td>
                                <td class="ft">
                                    <a href="song-9288-this-is-our-life.html">This Is Our Life</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-431-bosson.html'>Bosson</a>
                                </td>
                                <td class="ft">
                                    <a href="song-9286-all-because-of-you.html">All Because Of You</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-431-bosson.html'>Bosson</a>
                                </td>
                                <td class="ft">
                                    <a href="song-9285-i-don-t-wanna-say-goodbye.html">I Don't Wanna Say Goodbye</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-431-bosson.html'>Bosson</a>
                                </td>
                                <td class="ft">
                                    <a href="song-9284-stay.html">Stay</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-431-bosson.html'>Bosson</a>
                                </td>
                                <td class="ft">
                                    <a href="song-9283-let-your-soul-shine.html">Let Your Soul Shine</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                        </table>
                        <script type="text/javascript">
                        InitDataView("thelist", "#F7F7FF", "#FFFFFF");
                        </script>
                        <br/>
                        <div align="center" style="width:596px;">
                            <input type="button" value=" &lt;&lt; " class="button" onclick="document.location.href='search?mq=a+million&amp;mm=2&amp;si=0&amp;from=30'" style="cursor:hand"/>
                            <a href="search?mq=a+million&amp;mm=2&amp;si=0&amp;from=0" onfocus="this.blur()">1</a>
                            <font color="black"> | </font>
                            <a href="search?mq=a+million&amp;mm=2&amp;si=0&amp;from=30" onfocus="this.blur()">2</a>
                            <font color="black"> | </font>
                            <b>3</b>
                            <font color="black"> | </font>
                            <a href="search?mq=a+million&amp;mm=2&amp;si=0&amp;from=90" onfocus="this.blur()">4</a>
                            <input type="button" value=" &gt;&gt; " class="button" onclick="document.location.href='search?mq=a+million&amp;mm=2&amp;si=0&amp;from=90'" style="cursor:hand"/>
                        </div>
                        <script type="text/javascript">
                        document.getElementById('mq').focus();
                        </script>
                    </td>
                </tr>
            </table>
            <table width="100%" cellspacing="0" cellpadding="2">
                <tr>
                    <td align="center" style="border-top:2px dashed #E0E0E0;font-family:verdana, arial;font-size:12px;">
                    All lyrics are property and copyright of their owners.
                    </td>
                </tr>
            </table>
        </div>
    </center>

    <script>
    (function(i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] || function() {
            (i[r].q = i[r].q || []).push(arguments)
        },
        i[r].l = 1 * new Date();
        a = s.createElement(o),
        m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
    })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

    ga('create', 'UA-319914-9', 'auto');
    ga('send', 'pageview');
    </script>
</body>
</html>

"""

p4 = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <title>MLDb, The Music Lyrics Database - Advanced search</title>
    <meta name="Author" content="Nikolay Pelov, NickSoft"/>
    <meta name="Description" content="MLDb - Advanced search. Searching for &amp;quot;a million&amp;quot;"/>
    <meta name="Keywords" content="music,song,lyrics,mldb"/>
    <meta name="robots" content="index,follow"/>
    <meta name="revisit-after" content="7 days"/>
    <meta name="title" content="MLDb, The Music Lyrics Database - Advanced search"/>
    <meta name="distribution" content="Global"/>
    <meta name="rating" content="general"/>
    <link href="style.css" media="all" type="text/css" rel="stylesheet"/>
    <link href="/favicon.ico" rel="shortcut icon"/>
    <link rel="search" type="application/opensearchdescription+xml" href="http://www.mldb.org/opensearch.xml" title="MLDb music lyrics search"/>
    <!-- music song lyrics database begins -->
    <!-- music song lyrics database navigation links -->
    <link rel="MLDb - Home" title="Music lyrics" href="http://www.mldb.org/"/>
    <link rel="section" title="Music lyrics Search" href="http://www.mldb.org/search"/>
    <link rel="section" title="Top 40 Music Lyrics" href="http://www.mldb.org/top40.html"/>
    <link rel="section" title="Latest Music Lyrics" href="http://www.mldb.org/new-lyrics.html"/>
    <link rel="section" title="Submit music lyrics to database" href="http://www.mldb.org/submit.html"/>
    <link rel="contents" title="Extras: toolbar buttons, firefox search box" href="http://www.mldb.org/extras.html"/>
    <style type="text/css">
        <!--
        .dnone{
          display:none;
        }
        -->
        
    </style>
    <!-- International portal to music lyrics. Sorted lyrics by artist name. Clean and easy-to-use site with over 220,000 lyrics -->
    <!-- Top 40 lyrics chart. Comprehensive music lyrics search engine. Fulltext lyrics search. Search by artist, title, both of them or song lyrics -->
    <!-- <link rel="prefetch" href="http://"> -->
    <script type="text/javascript" src="js/main.js?v=3"></script>
    <script type="text/javascript" src="/js/ST.min.js?v=2"></script>
</head>
<body style="margin: 0px; padding: 0px;">
    <center>
        <div id="container">
            <table id="toptbl" align="center" cellspacing="0">
                <tr>
                    <td>
                        <!--<img src='img/headerbg.png' id="topimg" />-->
                        <div id="topadframe">
                            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9307576326974516" crossorigin="anonymous"></script>
                            <!-- MLDb top 468x60 -->
                            <ins class="adsbygoogle" style="display:inline-block;width:468px;height:60px" data-ad-client="ca-pub-9307576326974516" data-ad-slot="9720604683"></ins>
                            <script>
                            (adsbygoogle = window.adsbygoogle || []).push({});
                            </script>
                        </div>
                        <div id="toplinks" style="width:200px;position:absolute;">
                            <a href="/advertise.html" style="color:orange">Advertise</a>
                            <a href='/contact.html'>contact us</a>
                        </div>
                        <div style="height:80px"></div>
                        <div id="nav">
                            <div style="height:6px">
                                <img alt="" src="img/spacer.gif" width="1" height="6"/>
                            </div>
                            <div id="tabs" align="left">
                                <ul>
                                    <li>
                                        <a href="/" title="Music Lyrics Database Homepage">home</a>
                                    </li>
                                    <li>
                                        <a href="/aza-A.html" title="Complete artist list">artists</a>
                                    </li>
                                    <li>
                                        <a href="/azl-A.html" title="Complete album list">albums</a>
                                    </li>
                                    <li>
                                        <a href="/search?v=3" title="Search for song lyrics, detailed search" class="active">search</a>
                                    </li>
                                    <li>
                                        <a href="/top40.html" title="Top Chart of Music Lyrics Database">top 40</a>
                                    </li>
                                    <li>
                                        <a href="/new-lyrics.html" title="New lyrics">new</a>
                                    </li>
                                    <li>
                                        <a href="/submit.html" title="Submit new lyrics - help to make the world biggest music lyrics collection" style="color:#FFE090;">submit</a>
                                    </li>
                                    <li>
                                        <a href="/extras.html" title="Browser toolbars, buttons, search boxes." style="border-right: 1px solid rgb(119, 119, 119);">extras</a>
                                    </li>
                                </ul>
                            </div>
                            <div class="underline">
                                <img src="img/spacer.gif" alt="Main menu" height="2" width="1"/>
                            </div>
                            <!--  <div style="border-left: 1px solid rgb(119, 119, 119); float: left; height: 1px;"></div>-->
                            <div id="ajaxNav">
                                <div id="az" class="slip">
                                    <ul>
                                        <li>
                                            <a href="aza-0.html">#</a>
                                            <a href="aza-A.html">A</a>
                                            <a href="aza-B.html">B</a>
                                            <a href="aza-C.html">C</a>
                                            <a href="aza-D.html">D</a>
                                            <a href="aza-E.html">E</a>
                                            <a href="aza-F.html">F</a>
                                            <a href="aza-G.html">G</a>
                                            <a href="aza-H.html">H</a>
                                            <a href="aza-I.html">I</a>
                                            <a href="aza-J.html">J</a>
                                            <a href="aza-K.html">K</a>
                                            <a href="aza-L.html">L</a>
                                            <a href="aza-M.html">M</a>
                                            <a href="aza-N.html">N</a>
                                            <a href="aza-O.html">O</a>
                                            <a href="aza-P.html">P</a>
                                            <a href="aza-Q.html">Q</a>
                                            <a href="aza-R.html">R</a>
                                            <a href="aza-S.html">S</a>
                                            <a href="aza-T.html">T</a>
                                            <a href="aza-U.html">U</a>
                                            <a href="aza-V.html">V</a>
                                            <a href="aza-W.html">W</a>
                                            <a href="aza-X.html">X</a>
                                            <a href="aza-Y.html">Y</a>
                                            <a href="aza-Z.html">Z</a>
                                            <a href="aza-_.html">*</a>
                                        </li>

                                    </ul>
                                </div>
                            </div>
                        </div>
                    </td>
                </tr>
            </table>
            <table id="centertbl" align="center" cellspacing="0">
                <tr>
                    <td colspan="2" class="center">
                        <!-- page IS safe center -->
                        <div style="width:728px;height:90px;margin:auto">
                            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9307576326974516" crossorigin="anonymous"></script>
                            <!-- MLDb below top nav 728x90 -->
                            <ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-9307576326974516" data-ad-slot="5179889214"></ins>
                            <script>
                            (adsbygoogle = window.adsbygoogle || []).push({});
                            </script>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td class="leftplane">
                        <div style="width:160px">
                            <!-- Left Nav -->
                            <script type="text/javascript">
                            searchBox();
                            </script>
                            <br/>
                            <br/>
                            <script type="text/javascript">
                            drawStats(236679, 24057, 11223, 183);
                            </script>
                            <br/>
                            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9307576326974516" crossorigin="anonymous"></script>
                            <!-- MLDB Left Sidebar 160x600 -->
                            <ins class="adsbygoogle" style="display:inline-block;width:160px;height:600px" data-ad-client="ca-pub-9307576326974516" data-ad-slot="7838877680"></ins>
                            <script>
                            (adsbygoogle = window.adsbygoogle || []).push({});
                            </script>
                            <br/>
                            <br/>
                            <table class="main_tbl" cellspacing="0" style="width:160px">
                                <thead>
                                    <tr>
                                        <td>Top artists</td>
                                    </tr>
                                </thead>
                                <tr>
                                    <td>
                                        <a href='artist-3796-a-funny-thing-happened-on-the-way-to-the-forum-soundtrack.html?nc=1'>A Funny Thing Happened on the Way to the Forum Soundtrack</a>
                                        <br/>
                                        <a href='artist-25-metallica.html?nc=1'>Metallica</a>
                                        <br/>
                                        <a href='artist-278-a.html?nc=1'>A</a>
                                        <br/>
                                        <a href='artist-3795-a-charlie-brown-christmas-soundtrack.html?nc=1'>A Charlie Brown Christmas Soundtrack</a>
                                        <br/>
                                        <a href='artist-3807-fame-soundtrack.html?nc=1'>Fame Soundtrack</a>
                                        <br/>
                                    </td>
                                </tr>
                            </table>
                            <br/>
                            <table class="main_tbl" cellspacing="0" style="width:160px">
                                <thead>
                                    <tr>
                                        <td>Top albums</td>
                                    </tr>
                                </thead>
                                <tr>
                                    <td>
                                        <a href='album-12771-a-funny-thing-happened-on-the-way-to-the-forum-soundtrack.html?nc=1'>A Funny Thing Happened on the Way to the Forum Soundtrack</a>
                                        <br/>
                                        <a href='album-21665-a-arte-de-leila-pinheiro.html?nc=1'>A Arte de Leila Pinheiro</a>
                                        <br/>
                                        <a href='album-13642-por-siempre-tu-y-yo.html?nc=1'>Por siempre tu y yo</a>
                                        <br/>
                                        <a href='album-466-a.html?nc=1'>A</a>
                                        <br/>
                                        <a href='album-19150-piron.html?nc=1'>Piron</a>
                                        <br/>
                                    </td>
                                </tr>
                            </table>
                            <br/>

                            <table class="main_tbl" cellspacing="0" style="width:160px">
                                <thead>
                                    <tr>
                                        <td>External Links</td>
                                    </tr>
                                </thead>
                                <tr>
                                    <td>
                                        <a href="http://www.mybestmatch.net/" target="_blank" title="A new, fresh dating site.">MyBestMatch.net</a>
                                        <br/>
                                        <a href="http://www.bianca-ryan.org/" target="_blank">Bianca Ryan fan site</a>
                                        <br/>
                                        <a href="http://video.croler.net/" title="Search for online videos - music, movie trailers, home videos" target="_blank">Croler Video Search</a>
                                        <br/>
                                        <script type="text/javascript">
                                        </script>
                                    </td>
                                </tr>
                            </table>
                        </div>
                    </td>
                    <td class="centerplane">
                        <form action="search" method="get">
                            <table id="search_form">
                                <tr>
                                    <td nowrap="nowrap">
                                        <input type="text" id="mq" name="mq" style="width:360px;" value="a million"/>
                                        <input type="submit" value="Search" style="font-weight:bold;"/>
                                        <input type="submit" name="btnI" value="I'm Feeling Lucky"/>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <table cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td nowrap="nowrap">
                                                    <input type="radio" name="si" id="sft" value="3"/>
                                                    <label for="sft">
                                                        <b>Fulltext</b>
                                                    </label>
                                                    <input type="radio" name="si" id="sar" value="1"/>
                                                    <label for="sar"> Artist</label>
                                                    <input type="radio" name="si" id="sti" value="2"/>
                                                    <label for="sti"> Title</label>
                                                    <input type="radio" name="si" id="sfl" value="0" checked="checked"/>
                                                    <label for="sfl"> Artist and title</label>
                                                    <br/>
                                                    <input type="radio" name="mm" id="mmall" value="0"/>
                                                    <label for="mmall"> All words</label>
                                                    <input type="radio" name="mm" id="mmany" value="1"/>
                                                    <label for="mmany"> Any word</label>
                                                    <input type="radio" name="mm" id="mmphrase" value="2" checked="checked"/>
                                                    <label for="mmphrase"> Exact phrase</label>
                                                </td>
                                                <td>&nbsp;</td>
                                                <td valign="top">Sort by:</td>
                                                <td>
                                                    <input type="radio" name="ob" id="obr" value="1" checked="checked"/>
                                                    <label for="obr"> Relevance</label>
                                                    <br/>
                                                    <input type="radio" name="ob" id="oba" value="2"/>
                                                    <label for="oba"> Rating</label>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </form>

                        <table id="thelist" cellspacing="0">
                            <tr>
                                <th>Artist(s)</th>
                                <th>Song</th>
                                <th width="20">Rating</th>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-431-bosson.html'>Bosson</a>
                                </td>
                                <td class="ft">
                                    <a href="song-9282-we-live.html">We Live</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-431-bosson.html'>Bosson</a>
                                </td>
                                <td class="ft">
                                    <a href="song-9281-over-the-mountains.html">Over The Mountains</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-431-bosson.html'>Bosson</a>
                                </td>
                                <td class="ft">
                                    <a href="song-9280-where-are-you.html">Where Are You?</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-431-bosson.html'>Bosson</a>
                                </td>
                                <td class="ft">
                                    <a href="song-9279-i-believe.html">I Believe</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2625-came-to-give-love.html">Came To Give Love</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2624-the-one-i-gave-my-heart-to.html">The One I Gave My Heart To</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2623-ladies-in-da-house.html">Ladies In Da House</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2622-never-comin-back.html">Never Comin' Back</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2621-heartbroken.html">Heartbroken</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2620-never-givin-up.html">Never Givin' Up</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2619-i-gotcha-back.html">I Gotcha Back</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2618-giving-you-more.html">Giving You More</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2617-everythings-gonna-be-alright.html">Everythings Gonna Be Alright</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2616-4-page-letter.html">4 Page Letter</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2615-got-to-give-it-up.html">Got To Give It Up</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2614-choosey-lover-old-school-new-school.html">Choosey Lover (Old School/New School)</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2613-if-your-girl-only-knew.html">If Your Girl Only Knew</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="n">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2612-a-girl-like-you.html">A Girl Like You</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                            <tr class="h">
                                <td class="fa">
                                    <a href='artist-280-aaliyah.html'>Aaliyah</a>
                                </td>
                                <td class="ft">
                                    <a href="song-2610-hot-like-fire.html">Hot Like Fire</a>
                                </td>
                                <td align="right">-</td>
                            </tr>
                        </table>
                        <script type="text/javascript">
                        InitDataView("thelist", "#F7F7FF", "#FFFFFF");
                        </script>
                        <br/>
                        <div align="center" style="width:596px;">
                            <input type="button" value=" &lt;&lt; " class="button" onclick="document.location.href='search?mq=a+million&amp;mm=2&amp;si=0&amp;from=60'" style="cursor:hand"/>
                            <a href="search?mq=a+million&amp;mm=2&amp;si=0&amp;from=0" onfocus="this.blur()">1</a>
                            <font color="black"> | </font>
                            <a href="search?mq=a+million&amp;mm=2&amp;si=0&amp;from=30" onfocus="this.blur()">2</a>
                            <font color="black"> | </font>
                            <a href="search?mq=a+million&amp;mm=2&amp;si=0&amp;from=60" onfocus="this.blur()">3</a>
                            <font color="black"> | </font>
                            <b>4</b>
                            <input type="button" value=" &gt;&gt; " class="button" disabled="disabled" onclick="document.location.href='search?mq=a+million&amp;mm=2&amp;si=0&amp;from=0'" style="cursor:default"/>
                        </div>
                        <script type="text/javascript">
                        document.getElementById('mq').focus();
                        </script>
                    </td>
                </tr>
            </table>
            <table width="100%" cellspacing="0" cellpadding="2">
                <tr>
                    <td align="center" style="border-top:2px dashed #E0E0E0;font-family:verdana, arial;font-size:12px;">
                    All lyrics are property and copyright of their owners.
                    </td>
                </tr>
            </table>
        </div>
    </center>

    <script>
    (function(i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] || function() {
            (i[r].q = i[r].q || []).push(arguments)
        },
        i[r].l = 1 * new Date();
        a = s.createElement(o),
        m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
    })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

    ga('create', 'UA-319914-9', 'auto');
    ga('send', 'pageview');
    </script>
</body>
</html>


"""

links = []

for p in [p1, p2, p3, p4]:
    soup = BeautifulSoup(p, 'html.parser')

    thelist_table = soup.find('table', id='thelist')

    # Extract all links
    links += [a['href'] for a in thelist_table.find_all('a', href=True) if a['href'][0] == 's']

    # Print the links
print(links)

