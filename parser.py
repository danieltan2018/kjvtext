import re
import sys
bookNum = 0
books = ['Old Testament.txt', 'Genesis.txt', 'Exodus.txt', 'Leviticus.txt', 'Numbers.txt', 'Deuteronomy.txt', 'Joshua.txt', 'Judges.txt', 'Ruth.txt', '1 Samuel.txt', '2 Samuel.txt', '1 Kings.txt', '2 Kings.txt', '1 Chronicles.txt', '2 Chronicles.txt', 'Ezra.txt', 'Nehemiah.txt', 'Esther.txt', 'Job.txt', 'Psalm.txt', 'Proverbs.txt', 'Ecclesiastes.txt', 'Song of Songs.txt', 'Isaiah.txt', 'Jeremiah.txt', 'Lamentations.txt', 'Ezekiel.txt', 'Daniel.txt', 'Hosea.txt', 'Joel.txt', 'Amos.txt', 'Obadiah.txt', 'Jonah.txt', 'Micah.txt',
         'Nahum.txt', 'Habakkuk.txt', 'Zephaniah.txt', 'Haggai.txt', 'Zechariah.txt', 'Malachi.txt', 'New Testament.txt', 'Matthew.txt', 'Mark.txt', 'Luke.txt', 'John.txt', 'Acts.txt', 'Romans.txt', '1 Corinthians.txt', '2 Corinthians.txt', 'Galatians.txt', 'Ephesians.txt', 'Philippians.txt', 'Colossians.txt', '1 Thessalonians.txt', '2 Thessalonians.txt', '1 Timothy.txt', '2 Timothy.txt', 'Titus.txt', 'Philemon.txt', 'Hebrews.txt', 'James.txt', '1 Peter.txt', '2 Peter.txt', '1 John.txt', '2 John.txt', '3 John.txt', 'Jude.txt', 'Revelation.txt']
title = books[bookNum]
blankLines = 0
bookStore = ''
flag = False

with open('kjv.txt', 'r') as kjv:
    for line in kjv:
        line = line.strip()
        if line == '':
            blankLines += 1
        else:
            if re.search('\d+[:]\d+', line):
                temp = re.split('\d+[:]\d+', line)
                for i in range(len(temp)):
                    item = temp[i]
                    item = item.strip()
                    if item != '':
                        if i == 0:
                            bookStore += ' '
                        else:
                            bookStore += '\n'
                        bookStore += item
                    elif i == (len(temp) - 1):
                        flag = True
            elif blankLines <= 2:
                if flag:
                    bookStore += '\n'
                    flag = False
                else:
                    bookStore += ' '
                bookStore += line
            elif blankLines <= 4:
                with open(title, 'w+') as bookFile:
                    bookStore = bookStore.strip()
                    bookFile.write(bookStore)
                bookStore = ''
                bookNum += 1
                title = books[bookNum]
            else:
                with open(title, 'w+') as bookFile:
                    bookStore = bookStore.strip()
                    bookFile.write(bookStore)
                sys.exit()
            blankLines = 0
