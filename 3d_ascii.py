import pyfiglet
from termcolor import colored

txtFont = """
        1. digital
        2. isometric1
        3. isometric2
        4. isometric3
        5. 3-d
        6. 3x5
        7. 5lineoblique
        8. acrobatic
        9. alligator
        10. alligator2
        11. alphabet
        12. avatar
        13. banner
        14. banner3-D
        15. banner3
        16. banner4
        17. barbwire
        18. basic
        19. bell
        20. big
        21. bigchief
        22. binary
        23. block
        24. bubble
        25. bulbhead
        26. calgphy2
        27. caligraphy
        28. catwalk
        29. chunky
        30. coinstak
        31. colossal
        32. computer
        33. contessa
        34. contrast
        35. cosmic
        36. cosmike
        37. cricket
        38. cyberlarge
        39. cybermedium
        40. cybersmall
        41. diamond
        42. doh
        43. doom
        44. dotmatrix
        45. drpepper
        46. eftichess
        47. eftifont
        48. eftipiti
        49. eftirobot
        50. eftitalic
        51. eftiwall
        52. eftiwater
        53. epic
        54. fender
        55. fourtops
        56. fuzzy
        57. goofy
        58. gothic
        59. graffiti
        60. hollywood
        61. invita
        62. isometric4
        63. italic
        64. ivrit
        65. jerusalem
        66. katakana
        67. kban
        68. larry3d
        69. lcd
        70. lean
        71. letters
        72. linux
        73. lockergnome
        74. madrid
        75. marquee
        76. maxfour
        77. mike
        78. mini
        79. mirror
        80. mnemonic
        81. morse
        82. moscow
        83. nancyj-fancy
        84. nancyj-underlined
        85. nancyj
        86. nipples
        87. ntgreek
        88. o8
        89. ogre
        90. pawp
        91. peaks
        92. pebbles
        93. pepper
        94. poison
        95. puffy
        96. pyramid
        97. rectangles
        98. relief
        99. relief2
        100. rev
        101. roman
        102. rot13
        103. rounded
        104. rowancap
        105. rozzo
        106. runic
        107. runyc
        108. sblood
        109. script
        110. serifcap
        111. shadow
        112. short
        113. slant
        114. slide
        115. slscript
        116. small
        117. smisome1
        118. smkeyboard
        119. smscript
        120. smshadow
        121. smslant
        122. smtengwar
        123. speed
        124. stampatello
        125. standard
        126. starwars
        127. stellar
        128. stop
        129. straight
        130. tanja
        131. tengwar
        132. term
        133. thick
        134. thin
        135. threepoint
        136. ticks
        137. ticksslant
        138. tinker-toy
        139. tombstone
        140. trek
        141. tsalagi
        142. twopoint
        143. univers
        144. usaflag
        145. weird
"""

print(txtFont)

font_text = ''
color_text = 'green'
text = str(input("Enter your text for Convert: "))
choice = input("Enter Number font[1 - 145]: ")

match choice:
    case "1":
        font_text  = 'digital'
    case "2":
        font_text = 'isometric1'
    case "3":
        font_text  = 'isometric2'
    case "4":
        font_text = 'isometric3'
    case "5":
        font_text = '3-d'
    case "6":
        font_text = '3x5'
    case "7":
        font_text = '5lineoblique'
    case "8":
        font_text = 'alligator'
    case  "10":
        font_text = 'alphabet'
    case "12":
        font_text = 'banner'
    case  "14":
        font_text = 'banner3'
    case  "16":
        font_text = 'barbwire'
    case "18":
        font_text = 'bell'
    case "20":
        font_text = 'big'
    case "21":
        font_text = 'bigchief'
    case "22":
        font_text = 'binary'
    case "23":
        font_text = ''
    case "24":
        font_text = ''
    case  "25":
        font_text = ''
    case "26":
        font_text = ''
    case "27":
        font_text = ''
    case "28":
        font_text = ''
    case "29":
        font_text = ''
    case "30":
        font_text = ''
    case  "31":
        font_text = ''
    case "32":
        font_text = ''
    case "33":
        font_text = ''
    case "34":
        font_text = ''
    case "35":
        font_text = ''
    case "36":
        font_text = ''
    case "37":
        font_text = ''
    case "38":
        font_text = ''
    case "39":
        font_text = ''
    case  "40":
        font_text = ''
    case "41":
        font_text = ''
    case "42":
        font_text = 'doh'
    case "43":
        font_text = ''
    case "44":
        font_text = ''
    case "45":
        font_text = ''
    case  "46":
        font_text = ''
    case "47":
        font_text = ''
    case "48":
        font_text = ''
    case  "49":
        font_text = ''
    case "50":
        font_text = ''
    case "51":
        font_text = ''
    case "52":
        font_text = ''
    case  "53":
        font_text = ''
    case "54":
        font_text = ''
    case "55":
        font_text = ''
    case "56":
        font_text = ''
    case "57":
        font_text = ''
    case "58":
        font_text = ''
    case "59":
        font_text = ''
    case "60":
        font_text = ''
    case "61":
        font_text = ''
    case "62":
        font_text = ''
    case "63":
        font_text = ''
    case "64":
        font_text = ''
    case "65":
        font_text = ''
    case "66":
        font_text = ''
    case "67":
        font_text = ''
    case "68":
        font_text = ''
    case "69":
        font_text = ''
    case "70":
        font_text = ''
    case "71":
        font_text = ''
    case "72":
        font_text = ''
    case "73":
        font_text = ''
    case "74":
        font_text = ''
    case "75":
        font_text = ''
    case "76":
        font_text = ''
    case "77":
        font_text = ''
    case "78":
        font_text = ''
    case "79":
        font_text = ''
    case "80":
        font_text = ''
    case "81":
        font_text = ''
    case "82":
        font_text = ''
    case "83":
        font_text = ''
    case "84":
        font_text = ''
    case "85":
        font_text = ''
    case "86":
        font_text = ''
    case "87":
        font_text = ''
    case "88":
        font_text = ''
    case "89":
        font_text = ''
    case "90":
        font_text = ''
    case "91":
        font_text = ''
    case "92":
        font_text = ''
    case "93":
        font_text = ''
    case "94":
        font_text = ''
    case "95":
        font_text = ''
    case "96":
        font_text = ''
    case "97":
        font_text = ''
    case "98":
        font_text = ''
    case "99":
        font_text = ''
    case "100":
        font_text = ''
    case "101":
        font_text = ''
    case "102":
        font_text = ''
    case "103":
        font_text = ''
    case "104":
        font_text = ''
    case "105":
        font_text = ''
    case "106":
        font_text = ''
    case "107":
        font_text = ''
    case "108":
        font_text = ''
    case "109":
        font_text = ''
    case "110":
        font_text = ''
    case "111":
        font_text = ''
    case "112":
        font_text = ''
    case "113":
        font_text = ''
    case "114":
        font_text = ''
    case "115":
        font_text = ''
    case "116":
        font_text = ''
    case "117":
        font_text = ''
    case "118":
        font_text = ''
    case "119":
        font_text = ''
    case "120":
        font_text = ''
    case "121":
        font_text = ''
    case "122":
        font_text = ''
    case "123":
        font_text = ''
    case "124":
        font_text = ''
    case "125":
        font_text = ''
    case "126":
        font_text = ''
    case "127":
        font_text = ''
    case "128":
        font_text = ''
    case "129":
        font_text = ''
    case "130":
        font_text = ''
    case "131":
        font_text = ''
    case "132":
        font_text = ''
    case "133":
        font_text = ''
    case "134":
        font_text = ''
    case "135":
        font_text = ''
    case "136":
        font_text = ''
    case "137":
        font_text = ''
    case "138":
        font_text = ''
    case "139":
        font_text = ''
    case "140":
        font_text = ''
    case "141":
        font_text = ''
    case "142":
        font_text = ''
    case "143":
        font_text = ''
    case "144":
        font_text = ''
    case "145":
        font_text = ''
    case _:
        print("The font doesn't match")


ascii_text = pyfiglet.figlet_format(text, font=font_text, width=200) # digital isometric1
print(colored(ascii_text, 'green'))
