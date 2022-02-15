target = 'eva, can I see bees in a cave'
for i in range(len(target)):
    target = target.replace('!','')
    target = target.replace('?','')
    target = target.replace(',','')
    target = target.replace(':','')
    target = target.replace(';','')
    target = target.replace('-','')
    target = target.replace(' ', '')
new_tar = target
new_tar = new_tar.lower()
new_target = new_tar[::-1]
#if new_tar == new_target:
 #   return True
#else:
 #   return False
print(new_tar)