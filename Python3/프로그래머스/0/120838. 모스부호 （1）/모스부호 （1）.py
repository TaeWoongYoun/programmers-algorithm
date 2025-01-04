def solution(letter):
    answer = ''
    morse = {
        ".-"   : "a", "-..." : "b", "-.-." : "c", "-.."  : "d", "."    : "e",
        "..-." : "f", "--."  : "g", "...." : "h", ".."   : "i", ".---" : "j",
        "-.-"  : "k", ".-.." : "l", "--"   : "m", "-."   : "n", "---"  : "o",
        ".--." : "p", "--.-" : "q", ".-."  : "r", "..."  : "s", "-"    : "t",
        "..-"  : "u", "...-" : "v", ".--"  : "w", "-..-" : "x", "-.--" : "y", "--.." : "z"
    }
    letter = letter.split()
    for i in letter:
        if i in morse:
            answer += morse[i]
    return answer