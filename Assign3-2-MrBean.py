from tkinter import *
root = Tk()

canvas_width = 810
canvas_height = 780
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("MR.Bean")
root.maxsize(810,780)
root.minsize(810,780)
cartoon = Canvas(root, width=canvas_width, height=canvas_height)
cartoon.pack()

# outline black dark shadow
cartoon.create_polygon(483,635,475,635,465,637,455,637,448,637,439,637,431,635,421,635,411,635,403,635,393,635,384,635,376,635,369,635,360,637,352,635,353,628,351,621,351,614,349,609,348,600,348,590,348,579,346,568,346,559,348,549\
                        ,348,538,349,528,351,517,352,506,353,497,353,486,356,473,359,463,362,455,362,445,366,437,369,428,375,421,379,414,383,407,383,398,382,390,377,382,372,375,362,372,352,370,344,367,335,365,327,362,317,360,310,358\
                        ,303,352,296,348,287,341,280,335,274,325,270,314,270,303,270,294,272,287,265,280,258,276,249,270,241,263,234,255,226,248,221,238,217,226,214,215,215,207,218,195,226,187,235,181,243,179,253,177,265,179,274,180\
                        ,280,181,279,176,276,169,274,157,274,157,272,146,270,135,270,122,273,112,276,105,283,100,287,93,294,90,304,90,310,88,315,83,324,77,332,70,341,66,352,63,359,59,370,54,377,53,387,52,397,50,407,49,415,46,425,46\
                        ,434,46,444,46,453,46,465,47,475,49,486,49,496,52,506,56,516,56,524,62,532,64,537,71,544,78,545,84,551,88,559,86,568,88,576,93,583,100,589,108,592,118,593,126,593,136,593,143,593,149,590,156,589,164,586,169\
                        ,592,167,597,166,607,166,617,166,624,169,633,173,641,180,645,187,648,198,648,207,645,214,641,222,640,228,635,235,631,241,625,248,618,255,613,259,607,265,600,269,593,274,586,277,578,281,569,284,562,287,554,289\
                        ,548,290,542,290,539,297,537,304,531,308,528,312,523,318,518,322,514,325,510,329,506,331,501,336,496,342,487,345,479,349,472,353,466,355,461,359,453,363,448,369,441,375,439,380,438,389,438,394,439,398,441,406\
                        ,446,410,451,417,458,422,463,431,466,438,468,444,470,449,472,455,472,463,473,469,476,476,476,484,476,493,477,501,480,508,480,517,482,525,480,531,480,538,480,547,482,555,483,563,483,570,483,578,486,585,486,593\
                        ,487,600,484,609,480,613,477,618,476,625,479,630,482,633)

# main face
cartoon.create_polygon(425,401,421,403,414,406,407,406,400,406,394,403,394,396,393,387,391,376,383,370,376,365,367,359,360,359\
                        ,351,356,342,353,335,352,327,349,321,348,314,344,308,341,301,336,294,331,286,324,283,315,281,304,283,293\
                        ,284,286,287,279,291,270,293,263,298,253,300,246,301,236,301,224,300,214,297,207,296,198,294,188,291,176\
                        ,291,164,293,156,294,145,297,138,301,129,305,119,310,114,314,105,315,105,320,108,328,109,335,111,344,112\
                        ,351,114,358,114,366,114,373,114,380,117,386,115,394,115,401,115,410,117,418,117,422,115,430,115,438,114\
                        ,445,112,453,109,462,109,466,108,473,108,482,107,489,107,494,105,503,105,511,105,520,104,525,104,531,102\
                        ,531,105,528,111,525,119,525,125,525,133,528,139,528,146,530,150,531,157,532,163,532,170,534,174,534,181\
                        ,534,187,534,193,535,198,534,205,534,212,532,218,531,225,528,229,530,231,535,222,538,219,542,214,548,210\
                        ,555,203,561,195,565,193,572,190,578,186,583,184,587,181,596,180,604,179,613,179,621,181,630,184,635,191\
                        ,635,198,635,205,635,212,631,219,627,226,623,231,618,236,613,242,609,249,604,253,597,256,590,260,586,266\
                        ,578,269,569,273,561,276,552,276,545,279,537,280,532,284,530,289,527,296,523,301,517,305,513,311,508,315\
                        ,504,318,500,321,496,325,489,329,482,334,476,336,469,342,465,344,459,346,453,352,445,355,441,359,435,363\
                        ,432,369,430,376,427,380,427,387,427,393,fill="#ffcc99")

# left ear
cartoon.create_polygon(296,203,290,198,284,195,277,193,272,191,265,188,258,188,250,188,245,190,239,193,235,195,229,200,225,204,225\
                        ,210,226,217,226,224,231,231,235,238,241,245,246,250,252,256,259,262,265,267,272,270,279,276,284,279,289,276\
                        ,291,269,296,262,300,253,301,246,303,239,303,231,301,222,300,215,300,211,297,205,fill="#ffcc99")

# left side coat
cartoon.create_polygon(396,403,396,410,393,414,391,421,387,424,384,427,380,432,376,432,376,439,376,445,376,452,375,459,370,461,369,466\
                        ,369,473,367,482,366,489,365,496,365,500,363,507,363,514,362,520,360,528,360,537,360,542,359,549,359,556,358,565\
                        ,358,573,358,579,358,585,359,593,359,599,365,599,366,599,366,603,367,610,366,617,365,625,365,628,369,625,372,618\
                        ,375,613,377,604,379,597,380,590,380,582,380,573,382,563,383,555,384,545,386,535,387,527,387,518,389,511,390,501\
                        ,390,493,391,483,391,476,393,469,394,462,393,455,394,446,394,441,394,432,394,425,fill="#704110")

cartoon.create_polygon(394,406,380,558,377,480,386,468,377,455,394,406,width=3,outline="black",fill="#704110")
# right side coat
cartoon.create_polygon(427,401,427,406,428,413,428,420,428,425,428,432,427,439,427,449,427,456,428,465,428,472,427,479,428,487,428,490,428\
                        ,497,428,504,427,507,427,514,427,521,427,527,427,532,427,539,427,548,428,555,428,559,430,565,431,570,431,575,431,582\
                        ,431,586,434,593,434,599,435,606,435,611,438,617,439,624,445,628,451,625,449,618,449,611,446,604,451,599,456,594,463\
                        ,596,469,597,472,594,472,587,470,579,470,570,470,562,470,552,470,541,469,531,469,523,469,511,468,501,465,492,463,483\
                        ,462,475,462,466,459,458,456,451,455,442,452,435,446,430,441,422,435,418,431,413,outline="black",width=5,fill="#704110")

cartoon.create_polygon(428,411,441,452,432,462,441,475,430,552,428,411,width=3,outline="black",fill="#704110")

# white shirt of suit
cartoon.create_polygon(428,555,422,555,415,556,410,554,404,554,396,554,387,555,382,554,383,547,387,539,387,531,387,521,389,511,390,503,390,493\
                        ,393,483,393,476,393,466,394,456,394,448,394,438,394,428,396,420,396,411,396,404,400,403,406,406,414,406,418,403,425,403\
                        ,427,408,427,414,427,421,427,428,427,434,427,442,427,449,427,456,427,463,425,470,427,477,427,484,427,490,428,496,427,504\
                        ,427,511,427,518,427,525,427,531,427,538,428,544,430,549,fill="white")

# Tie of suit
cartoon.create_polygon(407,407,397,421,407,437,393,511,410,544,425,511,407,438,418,422,407,406,fill="red",outline="black",width=3)

# left eyebro and nose
cartoon.create_line(297,164,298,157,301,149,307,142,312,139,318,136,328,136,335,140,341,146,348,150,352,156,358,160,363,167,367,174,372,183,376,188\
                    ,377,197,379,205,380,214,382,222,380,229,380,238,379,245,377,252,375,259,372,265,369,269,365,273,360,276,358,281,356,289,358,296\
                    ,359,303,363,308,369,314,375,318,382,321,390,322,397,321,404,317,411,314,415,308,417,303,422,301,430,303,438,303,444,298,451,294\
                    ,452,287,449,279,444,273,438,272,431,272,425,273,420,274,width=4)

# some another part of nose
cartoon.create_line(363,274,356,272,351,272,345,273,341,277,338,281,338,289,336,296,344,301,349,303,356,304,width=4)

# right eyebro
cartoon.create_line(411,224,411,217,413,210,415,203,418,197,422,188,428,184,434,177,439,174,445,169,451,167,456,166\
                    ,462,166,469,164,477,162,484,157,492,157,497,157,503,160,510,164,514,170,516,177,width=4)

# one line of forhead
cartoon.create_line(332,121,338,119,345,119,352,122,359,125,366,128,373,132,380,133,386,136,394,138,403,139,407,139,width=4)

# another long line of forhead
cartoon.create_line(324,128,329,126,336,126,345,128,352,128,358,132,363,135,369,139,375,142,382,145,389,146,396,148,403,149,410,149,418,149,425,149,432\
                    ,148,441,145,446,143,453,142,461,139,468,139,475,139,482,139,490,140,499,142,width=4)

# mouth bg part
cartoon.create_polygon(441,304,434,305,428,307,422,305,418,311,413,317,407,321,400,325,393,327,386,325,377,322,369,320,362,314,355,308,348,307,345,311,338\
                        ,315,332,320,328,325,325,331,324,338,325,344,332,348,338,351,344,353,351,355,359,358,367,358,376,358,384,358,393,356,400,353,407,352\
                        ,415,348,422,345,430,339,435,334,439,328,445,321,445,314,445,307,fill="#e0a66c")

# smile part
cartoon.create_line(363,344,359,346,355,348,349,348,345,348,339,346,336,342,338,335,344,331,352,329,359,329,367,329,375,328,382,329,390,331,398,331,406,335,width=4)

# left ear fold part
cartoon.create_polygon(300,232,291,229,286,226,280,224,273,221,267,218,260,218,253,217,248,221,249,228,250,235,253,242,259,249,266,253,272,258,279,262,286,266\
                        ,289,267,283,266,280,265,277,263,273,260,269,258,263,253,258,248,252,245,249,239,246,234,243,231,242,225,242,218,245,212,248,207,255,204\
                        ,263,203,272,205,279,208,286,212,291,215,296,221,298,224)

# right ear fold part
cartoon.create_polygon(549,238,549,231,554,226,556,222,561,217,566,211,570,207,578,201,583,198,589,193,597,191,606,190,613,190,621,193,624,198,624,204,624,211,621\
                        ,218,618,224,616,229,611,232,607,236,602,243,596,248,589,252,583,255,578,256,572,260,563,263,558,263,551,266,545,266,539,262,541,256,542,252\
                        ,549,248,555,245,554,249,551,252,552,258,561,256,568,256,572,250,580,249,590,245,597,241,602,235,609,228,613,225,616,219,618,217,620,210,617\
                        ,204,611,203,606,203,600,204,594,205,587,211,580,214,575,218,568,221,563,224)

# sesame
cartoon.create_oval(480,280,487,286,width=8)

# line seperating neck
cartoon.create_line(394,403,404,406,411,404,418,404,425,401,width=4)

# line seperating left ear from main face
cartoon.create_line(294,188,294,197,296,204,298,211,301,218,303,226,301,235,301,243,298,250,296,258,293,265,290,270,287,274,width=4)

# left eye
cartoon.create_oval(308,192,372,257,fill="white",width=3)
cartoon.create_oval(350,232,357,237,width=12)
cartoon.create_polygon(307,235,305,228,305,221,307,214,311,207,315,203,322,198,329,194,336,193,345,193,352,194,359,200,365,205,370,211,372,219,372,228,372,229,369,229,362,232,355,231,348,232,342,232,335,232,329,234,324,234,318,234,311,234,fill="#e0a66c",outline="black",width=3)

# right eye
cartoon.create_oval(427,190,494,255,fill="white",width=3)
cartoon.create_oval(467,232,477,237,width=12)
cartoon.create_polygon(428,238,425,231,425,224,425,215,428,208,432,201,438,197,445,193,453,190,462,190,470,191,477,195,484,200,489,207,492,214,493,219,493,228,492,234,484,234,477,234,470,235,463,235,455,235,449,236,444,236,438,236,fill="#e0a66c",outline="black",width=3)


root.mainloop()