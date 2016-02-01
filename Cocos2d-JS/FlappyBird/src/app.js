
var gameLayer;
var bird;
var gameScene = cc.Scene.extend({
    onEnter:function () {
        this._super();
        gameLayer = new game();
        gameLayer.init();
        this.addChild(gameLayer);
    }
});
gameScene.prototype.reset = function() {
    this.removeChild(gameLayer);
    gameLayer = new game();
    gameLayer.init();
    this.addChild(gameLayer);
}


var game = cc.Layer.extend({
    init: function () {
        this._super();
        cc.eventManager.addListener({
            event: cc.EventListener.MOUSE,
            onMouseDown: function(event){
                bird.jump();
            }
        }, this)
        this.scoreText = cc.LabelTTF.create("0", "Arial", "45");
        this.scoreText.setPosition(WINDOW_WIDTH / 2, WINDOW_HEIGHT * 3 / 4);
        this.score = 0
        bird = new Bird();
        this.bg = cc.Sprite.create("res/bg.png");
        this.bg.setAnchorPoint(0, 0);
        this.land_bg = new ScrollingBG();
        this.landHeight = this.land_bg.getContentSize().height;
        this.gameHeight = WINDOW_HEIGHT - this.landHeight;
        this.addChild(this.bg);
        this.addChild(bird);
        this.addChild(this.land_bg, 1);
        for(var i = 0; i < 2; i++){
            var pipes = this.makePipes(WINDOW_WIDTH * 2 / 3 * (i + 2));
            this.addChild(pipes[0]);
            this.addChild(pipes[1]);
        }
        this.addChild(this.scoreText, 1);
        this.scheduleUpdate();
        },
    update: function(dt){
        this.land_bg.scroll();
    },
    reset: function(){
        bird.setPosition(bird.getPosition().x, bird.getPosition().y + 5);
    },
    makePipes: function(){
        if (arguments.length == 1){
            top_x = bottom_x =arguments[0];
        }
        else{
            top_x = bottom_x = WINDOW_WIDTH * 2;          
        }
        top_pipe = new PipeTop();
        bottom_pipe = new PipeBottom();
        var top_pipe_height = this.getRandomRange(this.gameHeight / 8, this.gameHeight / 3 * 2);
        var bottom_pipe_height = this.gameHeight - SPACE_PIPES - top_pipe_height;
        top_pipe.setPosition(top_x - top_pipe.getContentSize().width, WINDOW_HEIGHT - top_pipe_height);
        bottom_pipe.setPosition(bottom_x - bottom_pipe.getContentSize().width,
                                0 + this.landHeight- (bottom_pipe.getContentSize().height - bottom_pipe_height));
        return [top_pipe, bottom_pipe];
    },
    addPipes: function(){
        var pipes = this.makePipes(WINDOW_WIDTH * 2 / 3 * 2);
        this.addChild(pipes[0]);
        this.addChild(pipes[1]);
    },
    scoreInc: function(){
        this.score += 1;
        this.scoreText.setString(this.score);
    },
    getRandomRange: function(minimum, maximum){
        return Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;
    }
});

var ScrollingBG = cc.Sprite.extend({
    ctor:function() {
        this._super();
        this.initWithFile("res/land_bg.png");
    },
    onEnter:function() {
        this.setPosition(155, 64);
    },
    scroll:function(){
        this.setPosition(this.getPosition().
        x-SCROLLSPEED,this.getPosition().y);
        if(this.getPosition().x<0){
        this.setPosition(this.getPosition().x+180,this.getPosition().y);
    }
    }
});

var Bird = cc.Sprite.extend({
    ctor: function() {
        this._super();
        this.curJumpRate = 0;
        this.curJumpHeight = 0;
        this.velocity = 0;
        this.initWithFile("res/bird.png");
    },
    onEnter: function(){
        this._super();
        this.setAnchorPoint(0, 0);
        this.setPosition(WINDOW_WIDTH / 4, WINDOW_HEIGHT / 2);
        this.scheduleUpdate();
    },
    jump: function(){
        this.velocity = 0;
        this.curJumpRate += 1;
        //this.setPosition(bird.getPosition().x, bird.getPosition().y + 100);
    },
    update: function(){
        if (this.curJumpRate > 0){
            this.curJumpRate += 1;
            if (this.curJumpRate > JUMPRATE){
                this.curJumpRate = 0;
                this.curJumpHeight = 0;
            }
            this.curJumpHeight = this.getJumpAmount(this.curJumpRate);
        }
        this.velocity -= GRAVITY;
        this.setPosition(this.getPosition().x, this.getPosition().y + this.velocity + this.curJumpHeight);
    },
    getJumpAmount: function(curJumpRate){
        return Math.sin(Math.PI / JUMPRATE) * this.curJumpRate * JUMPHEIGHT;
    }
});

var Pipe = cc.Sprite.extend({
    ctor: function(){
        this._super();
        this.scheduleUpdate();
    },
    onEnter: function(){
        this._super();
        this.setAnchorPoint(0, 0);
    },
    update: function(){
        this.setPosition(this.getPosition().x - 2, this.getPosition().y);
        if (cc.rectIntersectsRect(this.getBoundingBox(), bird.getBoundingBox())){
            gameLayer.reset();
        }
    }
});

var PipeTop = Pipe.extend({
    ctor: function(){
        this._super();
        this.initWithFile("res/top_pipe.png");
    },
    update: function(){
        this._super();
        if(this.getPosition().x == bird.getPosition().x + 1){
            gameLayer.scoreInc();
        }
        if(this.getPosition().x < 0 - this.getContentSize().width){
            gameLayer.removeChild(this);
            gameLayer.addPipes();
        }
    }
});

var PipeBottom = Pipe.extend({
    ctor: function(){
        this._super();
        this.initWithFile("res/bottom_pipe.png");
    },
    update: function(){
        this._super();
        if(this.getPosition().x < 0 - this.getContentSize().width){
            gameLayer.removeChild(this);
        }        
    }
});