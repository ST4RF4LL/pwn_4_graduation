# include <stdio.h>

int menu()
{
    int c;
    puts("select your choice:");
    puts("1. Attack");
    puts("2. Defend");
    while(1)
    {
        printf(">");
        // c = getchar();
        scanf("%d",&c);
        getchar();
        if(c==1) return 1;
        if(c==2) return 2;
        else
        {
            puts("invalid choice!");
        }
    }
}

int vlun()
{
    char s[40];
    puts("Hero! Now, write something for your story!");
    gets(s);
    puts("What a wonderful ending!");
    return 0;
}

int story()
{
    char name[8];
    int dmg_warrior;
    int dmg_dragon;
    unsigned char hp_dragon;
    int hp_warrior;
    int armor_warrior;
    int regeneration_dragon;
    int choice;
    dmg_warrior = 0;
    dmg_dragon = 40;
    hp_dragon = 200;
    hp_warrior = 40;
    regeneration_dragon = 10;
    puts("Hello foreigner, could you please tell your name?");
    printf(">");
    // input(name,20);
    fgets(name,8,stdin);
    puts("All right foreigner, now that I know who you are, I have to tell you that there is a dragon getting in the way on your journey.");
    puts("You must kill the dragon, or everthing will be destoryed by the dragon. Take it! I think you need a sword");
    // getchar();
    dmg_warrior += 4;
    puts("[+]get weapon:sword,damage+4[+]");
    // getchar();
    puts("Now beat the dragon!!!");
    while(1)
    {
        printf("Dragon: hp:%d dmg:%d regeneration:%d\n",hp_dragon,dmg_dragon,regeneration_dragon);
        printf("You: hp:%d dmg:%d\n",hp_warrior,dmg_warrior);
        choice = menu();
        if(choice==1)
        {
            hp_dragon -= dmg_warrior;
            armor_warrior = 0;
        }
        if(choice==2)
        {
            armor_warrior = 35;
        }
        if(hp_dragon<=0)
        {
            puts("You win!");
            return 1;
        }
        hp_warrior-=(dmg_dragon-armor_warrior);
        if(hp_warrior<=0)
        {
            puts("Since no one can prevent the dragon,everything burned down.");
            return 0;
        }
        hp_dragon+=regeneration_dragon;
    }
    return 0;
}

int main()
{
    setvbuf(stdin,0,2,0);
    setvbuf(stdout,0,2,0);
    int flag;
    flag = story();
    if(flag)vlun();
    return 0;
}