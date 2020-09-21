# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image, ImageChops
import numpy

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):
        # get all the attribute and method for problem
        # print(problem.__dict__)
        # print(problem.figures['A'].__dict__)
        # print(problem.figures['A'].objects['a'].__dict__) # the objects under figure is the verbal description of an object in a figure, the 'a' is randomly assigned
        # print(problem.figures['A'].visualFilename) # this is file that required to solve the problem visually
        # test = Image.open(problem.figures['A'].visualFilename) # Load the image
        # pix = numpy.array(test)
        # print(pix.shape)
        FA = Image.open(problem.figures['A'].visualFilename)
        FB = Image.open(problem.figures['B'].visualFilename)
        FC = Image.open(problem.figures['C'].visualFilename)
        F1 = Image.open(problem.figures['1'].visualFilename)
        F2 = Image.open(problem.figures['2'].visualFilename)
        F3 = Image.open(problem.figures['3'].visualFilename)
        F4 = Image.open(problem.figures['4'].visualFilename)
        F5 = Image.open(problem.figures['5'].visualFilename)
        F6 = Image.open(problem.figures['6'].visualFilename)

        ModeAB = self.determine_Mode(FA, FB)
        ModeAC = self.determine_Mode(FA, FC)
        # print(f'ModeAB: {ModeAB}, ModeAC: {ModeAC}')

        ans_lst = [1,2,3,4,5,6]
        test_fig_lst = [F1, F2, F3, F4, F5, F6]
        score_lst = []
        for e in test_fig_lst:
            scoreCD, scoreBD = self.get_scores(ModeAB, ModeAC, FB, FC, e)
            # print(f'scoreCD: {scoreCD}, scoreBD: {scoreBD}')
            score_lst.append(scoreCD + scoreBD)

        min_index = score_lst.index( min(score_lst) )
        answer = ans_lst[min_index]

        return answer
        


    def find_diff(self, img1, img2):
        """ input is two image and returns sum of the diff numpy array"""
        delta12 = ImageChops.difference(img1, img2)
        delta12Numpy = numpy.array(delta12)

        return delta12Numpy

    def determine_Mode(self, img1, img2):
        """determine the mode of transformation between img1 and img2, varaitbles representing 
            specific transformation are scored and the oen with MIN(scores) will be returned"""
        nochange = self.find_diff(img1, img2).sum()
        flipLeftRight = self.find_diff( img1.transpose(Image.FLIP_LEFT_RIGHT), img2).sum()
        flipTopBottom = self.find_diff( img1.transpose(Image.FLIP_TOP_BOTTOM), img2).sum()
        rotate90 = self.find_diff( img1.transpose(Image.ROTATE_90), img2 ).sum()
        rotate180 = self.find_diff( img1.transpose(Image.ROTATE_180), img2 ).sum()
        rotate270 = self.find_diff( img1.transpose(Image.ROTATE_270), img2 ).sum()

        lst = [nochange, flipLeftRight, flipTopBottom, rotate90, rotate180, rotate270]
        min_index = lst.index( min(lst) )
        result_lst = ['nochange', 'FLIP_LEFT_RIGHT', 'FLIP_TOP_BOTTOM', 'ROTATE_90', 'ROTATE_180', 'ROTATE_270']
        result = result_lst[min_index]
        # print(result)
        return result

    def get_scores(self, modeAB, modeAC, imgB, imgC, TestImage):
        """This funciton uses the mode determined and test to get the best answer among Fig{1..6}"""
        if modeAB == 'nochange':
            scoreCD = self.find_diff(imgC, TestImage).sum()
        elif modeAB == 'FLIP_LEFT_RIGHT':
            scoreCD = self.find_diff( imgC.transpose(Image.FLIP_LEFT_RIGHT), TestImage).sum()
        elif modeAB == 'FLIP_TOP_BOTTOM':
            scoreCD = self.find_diff( imgC.transpose(Image.FLIP_TOP_BOTTOM), TestImage).sum()
        elif modeAB == 'ROTATE_90':
            scoreCD = self.find_diff( imgC.transpose(Image.ROTATE_90), TestImage ).sum()
        elif modeAB == 'ROTATE_180':
            scoreCD = self.find_diff( imgC.transpose(Image.ROTATE_180), TestImage ).sum()
        elif modeAB == 'ROTATE_270':
            scoreCD = self.find_diff( imgC.transpose(Image.ROTATE_270), TestImage ).sum()
        
        if modeAC == 'nochange':
            scoreBD = self.find_diff(imgB, TestImage).sum()
        elif modeAC == 'FLIP_LEFT_RIGHT':
            scoreBD = self.find_diff( imgB.transpose(Image.FLIP_LEFT_RIGHT), TestImage).sum()
        elif modeAC == 'FLIP_TOP_BOTTOM':
            scoreBD = self.find_diff( imgB.transpose(Image.FLIP_TOP_BOTTOM), TestImage).sum()
        elif modeAC == 'ROTATE_90':
            scoreBD = self.find_diff( imgB.transpose(Image.ROTATE_90), TestImage ).sum()
        elif modeAC == 'ROTATE_180':
            scoreBD = self.find_diff( imgB.transpose(Image.ROTATE_180), TestImage ).sum()
        elif modeAC == 'ROTATE_270':
            scoreBD = self.find_diff( imgB.transpose(Image.ROTATE_270), TestImage ).sum()

        # print(f'scoreCD: {scoreCD}, scoreBD: {scoreBD}')
        return scoreCD, scoreBD

        

        
        



        
