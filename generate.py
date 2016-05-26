import random
import sys
import string

alphabet = string.ascii_lowercase

names = ["Jacob", "Michael", "Joshua", "Matthew", "Ethan", "Andrew", "Daniel", 
		"Anthony", "Christopher", "Joseph", "William", "Alexander", "Ryan", "David", 
		"Nicholas", "Tyler", "James", "John", "Jonathan", "Nathan", "Emily", "Emma", 
		"Madison", "Abigail", "Olivia", "Isabella", "Hannah", "Samantha", "Ava", 
		"Ashley", "Sophia", "Elizabeth", "Alexis", "Grace", "Sarah", "Alyssa", "Mia", "Natalie", "Chloe", "Brianna"]

def getwords():
	words = open('NP-source/words.txt', 'r').readlines()
	return [w.strip() for w in words]

def randindex():
	return '14%04d' % random.randint(0, 9999)


def randstring(size = 10, alphanum = False, uppercase = False):
	res = ''
	letters = list(alphabet)
	letters_uppercase = list(alphabet.upper())
	x = '0123456789'
	digits = list(x)
	for i in range(size):
		l = letters
		if uppercase:
			upper = random.random()
			if upper > .7:
				l = letters_uppercase
		if alphanum:
			alpha = random.random()
			if alpha > .8:
				res += random.choice(digits)
			else:
				res += random.choice(l)
		else:	
			res += random.choice(l)
		
	return res
def rn(n):
	print n
	for i in range(n):
		print '%s' % random.choice(names)
		for j in range(4):
			for k in range(5):
				print '%d' % random.randint(30, 60),
			print

def rec(n):
	print n
	words = getwords()
	for i in range(n):
		print random.choice(words)

def pbt(n):
	prefixes = [70, 71, 75, 76, 77, 78]
	print n
	for i in range(n):
		print "%s:0%s" % (random.choice(names), str(random.choice(prefixes)) + str(random.randint(0, 999999)))

	for i in range(n / 3):
		if i % 2 == 0:
			print "%s:%s" % ("NAME", random.choice(names))
		else:
			print "%s:%s" % ("NUM", random.randint(100, random.randint(999, 99999)))

def bc(n, size):
	print n, size
	x = set()
	generated = 0
	while generated < n:
		number = random.randint(1, 5000)
		if number not in x:
			print number
			x.add(number)
			generated += 1
	generated = 0
	x = set()
	while  generated < n:
		size = random.randint(3, 10)
		s = randstring(size)
		if s not in x:
			print s
			x.add(s)
			generated += 1

def students(n):
	for i in range(n):
		print "%s\t%d\t%d\t%d\t%d\t%d" % (random.choice(names), 
			random.randint(100000, 150000), 
			random.randint(0, 100), random.randint(0, 100),
			random.randint(0, 100), random.randint(0, 100))

def checkIn(n):
	for i in range(n):
		sepDate = '.'
		sepTime = ':'
		x = random.random()
		if x > 0.8:
			sepDate = '/'
		if x < .3:
			sepTime = '.'
		date1 = randDate(separator = sepDate)
		time1 = randTime(hourEnd = 12, separator = sepTime)
		time2 = randTime(hourStart = 13, hourEnd = 23, separator = sepTime)
		date2 = date1
		if x > 0.4 and x < 0.45:
			date2 = randDate(separator = sepDate)

		if x > 0.5 and x < 0.55:
			time1, time2 = time2, time1

		print "%s %s-%s %s-%s" % (random.choice(names), date1, time1, date2, time2)

def points(n):
	END = 48 * 60
	team = 0
	team1 = "Heat"
	team2 = "Thunder"
	current_team = team1
	print "%s %s" % (team1, team2)
	time = 0
	while True:
		player = random.randint(4, 15)
		atack = random.randint(5, 24)
		time += atack
		if time >= END:
			return
		ap = random.random() * 100
		if ap <= 20:
			attempt = 1
		elif ap > 20 and ap <= 70:
			attempt = 2
		elif ap > 70:
			attempt = 3

		if attempt == 1:
			accuracy = random.randint(60, 98)	
			shoot = random.randint(0, 100)
			basket = 0
			if shoot <= accuracy:
				basket = 1
			print "%d %s %d %d %d" % (time, current_team, player, basket, attempt)			
			
		if attempt == 2:
			accuracy = random.randint(20, 80)	

		if attempt == 3:
			accuracy = random.randint(10, 60)	

		shoot = random.randint(0, 100)
		basket = 0
		if shoot <= accuracy:
			basket = 1
		print "%d %s %d %d %d" % (time, current_team, player, basket, attempt)			
		if team == 1: 
			current_team = team1
			team = 0
		else: 
			current_team = team2
			team = 1

def randDate(dayStart = 1, dayEnd = 30, monthStart = 1, monthEnd = 12, year = 2015, separator = '.'):
	return "%02d%s%02d%s%d" % (random.randint(dayStart, dayEnd), separator, 
		random.randint(monthStart, monthEnd), separator, year)

def randTime(hourStart = 0, hourEnd = 23, minuteStart = 0, minuteEnd = 59, separator = ':'):
	return "%02d%s%02d" % (random.randint(hourStart, hourEnd), separator, random.randint(minuteStart, minuteEnd))

def p11(n):
	print n
	for i in range(n):
		print randstring(random.randint(2, 80), False, True)

def matrica(m, n):
	print "%d %d" % (m, n)
	for i in range(m):
		for j in range(n):
			print "%d\t" % random.randint(1, 100),
		print

def matrica_kv(m):
	print "%d" % m
	for i in range(m):
		for j in range(m):
			print "%d\t" % random.randint(1, 100),
		print

def p13(n):
	added = set()
	indexes = set()
	for i in range(n):
		name = random.choice(names)
		if name not in added:
			print '%s %s %d' % (name, randindex(), random.randint(5, 10))
			added.add(name)

def p21(n):
	print n
	for i in range(n):
		x = random.randint(1, 50)
		print x,
		for j in range(x):
			print random.randint(100, 1000000),
		print

def calls(n):
	prefixes = [70, 71, 72, 75, 76, 77, 78, 88, 99]
	type = "I"
	for i in range(n):
		x = random.random()
		if x > 0.8:
			separator = '.'
		else:
			separator = ':'
		if x > 0.5:
			type = "O"
		else:
			type = "I"
		if x > 0.9:
			print "0%s%03d %02d%s%02d%s%02d %s" % (str(random.choice(prefixes)), random.randint(0, 999), 
			random.randint(0, 2), separator, random.randint(0, 60), separator, random.randint(0, 60), type)
		else:
			print "0%s%06d %02d%s%02d%s%02d %s" % (str(random.choice(prefixes)), random.randint(0, 999999), 
			random.randint(0, 2), separator, random.randint(0, 60), separator, random.randint(0, 60), type)

def br(n):
	for i in range(n):
		print '%d %d %d' % (random.randint(1, 50), random.randint(1, 50), random.randint(1, 50))

def trans():
	n = random.randint(50, 500)
	cur = ['MKD', 'USD', 'EUR']#, 'mkd', 'eur', 'usd']
	print n
	for i in range(n):
		print '%s %d %02d/%02d/%04d' % (random.choice(cur), (random.randint(1, 10000)) * random.choice([-1, 1, 2]), random.randint(1, 31), random.randint(1, 12), random.randint(2010, 2016))

def numbers(total_from = 5, total_to = 100, number_from = 1, number_to = 1000000):
	n = random.randint(total_from, total_to)
	print n
	for i in range(n):
		print '%d' % random.randint(number_from, number_to),
	
def numbers_sorted(total_from = 5, total_to = 100, number_from = 1, number_to = 1000000):
	n = random.randint(total_from, total_to)
	print n
	a = []
	for i in range(n):
		a.append(random.randint(number_from, number_to))
	a = sorted(a)
	for i in range(n):
		print '%d' % a[i],


def users(n):
	gen = set()
	x = '0123456789'
	digits = list(x)
	for i in range(n):
		user = randstring(5)
		if user in gen:
			continue
		gen.add(user)
		d = random.choice(digits)
		print 'insert into users (name) values (\'%s%c\');' % (user, d)

def text():
    n = random.randint(5, 50)
    for i in range(n):
        x = random.randint(10, 80)
        s = randstring(x, True, True)
        print s

def movies():
	n = random.randint(5, 500)
	print n
	movies = open('movies.txt').readlines()
	picked = set()
	while len(picked) != n:
		x = random.randint(0, len(movies) - 1)
		if x not in picked:
			picked.add(x)
			m = movies[x].strip()
			print m
			rc = random.randint(5, 100)
			print rc
			for r in range(rc):
				print random.randint(1, 10),
			print

def a():
	ap = open('airports.txt').readlines()
	print len(ap)
	l = []
	for a in ap:
		aa = a.strip()
		print aa
		l.append(aa.split(';')[2])
	n = random.randint(50, 500)
	print n
	for i in range(n):
		p = random.sample(l, 2)
		print '%s;%s;%d;%d' % (p[0], p[1], random.randint(0, 24 * 60), random.randint(30, 5 * 60))
	x = random.randint(0, len(ap))
	y = (x + random.randint(0, len(ap)))  % len(ap)
	print '%d %d' % (x, y)

def nn():
	n = random.randint(5, 100)
	print n
	for i in range(n):
		x = random.randint(5, 100)
		print x,
		for j in range(x):
			print random.randint(0, 30),
		print
def mm():
	n = random.randint(10, 30)
	for i in range(n):
		x = random.randint(0, 1)
		print x
		print random.randint(-120, 120), random.randint(-120, 120), random.randint(-5, 50),
		if x == 1:
			print random.randint(-5, 50)
		else:
			print
	print 2
def np16():
	courses = ['KNI', 'IKI', 'PET', 'MT']
	n = random.randint(50, 250)
	for i in range(n):
		print '%s%c %s' % (randstring(5), str(random.randint(0, 9)), random.choice(courses)),
		x = random.randint(5, 40)
		for j in range(x):
			print grade(),
		print



def grade():
	g = int(round(random.gauss(8, 1.5)))
	if g < 6:
		return 6
	elif g > 10:
		return 10
	return g

def cluster():
	n = random.randint(50, 250)
	print n
	for i in range(n):
		print '%d %f %f' % (i + 1, random.uniform(-20, 20), random.uniform(-20, 20))
	print random.randint(1, n), random.randint(5, 20)

if __name__ == "__main__":
#	if len(sys.argv) <= 1:
#		print 'Usage: %s [arguments]' % (sys.argv[0])
#	else:
	mm()

