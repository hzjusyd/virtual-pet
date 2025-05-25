# virtual-pet

the program mainly has the following functions:
1. Pets have multiple attributes, including the pet's name, hunger value, energy value, happiness value, age, whether it is sick, and optional food and games.
2. Feeding, choose a food to feed. If the selection is valid and the pet's hunger value is sufficient, the corresponding hunger value is reduced and the happiness value is increased, and the corresponding prompt information is output. If the pet is not hungry, it will prompt that it does not need to be fed; if the selection is invalid, it will prompt to re-enter.
3. Playing, choose a game to play, if the selection is valid and the pet's energy value is sufficient, the corresponding energy value is reduced and the happiness value is increased, and the corresponding prompt information is output. If the pet is too tired, it will prompt that it has no energy to play; if the selection is invalid, it will prompt to re-enter.
4. Sleeping, check whether the pet's energy value is less than or equal to 80. If so, increase 30 energy points, 10 hunger points, and increase 1 year old. There is a 10% probability that the pet will get sick after sleeping. If it is sick, a prompt message will be output. If the pet is energetic, it will prompt that it does not need to sleep.
5. Treatment method: If the pet is sick, change its status to healthy, increase happiness by 10 points, reduce energy by 15 points, and output a prompt message indicating successful treatment. If the pet is healthy, it will prompt that no treatment is needed.
6. Check the status and output the current status of the pet, including age, hunger value, energy value, happiness value, and whether it is sick.
