(() => {
    const STORAGE_KEY = "englishLadder.usLife.explanationLanguage";

    const languages = {
        ja: {
            label: "Japanese",
            lang: "ja",
            headingPrefix: "説明",
            rememberLabel: "大切なポイント",
            practiceLabel: "声に出す練習",
        },
        zh: {
            label: "Mandarin",
            lang: "zh-Hans",
            headingPrefix: "说明",
            rememberLabel: "重点",
            practiceLabel: "开口练习",
        },
    };

    const explanations = {
        arrival: {
            ja: {
                heading: "到着後すぐに必要な英語",
                points: [
                    "空港や駅では、短く正直に答えることが大切です。滞在先の住所、学校名、勤務先、緊急連絡先をすぐ見せられるようにしましょう。",
                    "聞き取れないときに、ゆっくり話してほしいと頼むのは失礼ではありません。低いレベルの学習者でも使える安全な表現です。",
                    "最初の一週間は、移動方法、携帯電話、家の鍵、近くのスーパー、緊急連絡先を先に確認すると安心です。",
                ],
                practice: "Could you please speak slowly?",
            },
            zh: {
                heading: "刚到美国时最需要的英语",
                points: [
                    "在机场或车站，回答要简短、真实。把住宿地址、学校或工作信息、紧急联系人准备好，方便马上出示。",
                    "听不懂时，请对方说慢一点并不失礼。这是低级别学习者也可以放心使用的表达。",
                    "第一周先确认交通方式、手机、钥匙、附近超市和紧急联系人，这样生活会稳定很多。",
                ],
                practice: "Could you please speak slowly?",
            },
        },
        documents: {
            ja: {
                heading: "書類は生活の土台",
                points: [
                    "アメリカでは、住所、身分証明、署名、期限がとても重要です。書類の写真だけでなく、紙のコピーも安全な場所に保管しましょう。",
                    "移民関係の情報は必ず公式サイト、学校の担当者、または資格のある弁護士に確認します。SNSだけを信じないでください。",
                    "多くの外国人は引っ越し後にUSCISへ住所変更をする必要があります。郵便局の転送だけではUSCISの住所は変わりません。",
                ],
                practice: "Is this the official website?",
            },
            zh: {
                heading: "文件是美国生活的基础",
                points: [
                    "在美国，地址、身份证明、签名和截止日期都很重要。重要文件要保存电子版，也要把纸质复印件放在安全的地方。",
                    "移民信息要查官方网站、学校负责人员，或合格律师。不要只相信社交媒体上的说法。",
                    "很多非公民搬家后需要向USCIS更新地址。只做邮局转寄，不会自动更新USCIS地址。",
                ],
                practice: "Is this the official website?",
            },
        },
        housing: {
            ja: {
                heading: "契約前に確認すること",
                points: [
                    "家賃だけでなく、保証金、光熱費、駐車場、洗濯、ペット、解約条件も確認します。英語が難しければ、署名前に時間をもらいましょう。",
                    "アメリカでは書面の記録が大切です。質問、修理依頼、支払いの証拠はメールや写真で残すと安心です。",
                    "ルームメイトと住む場合は、掃除、静かな時間、来客、共有品のルールを早めに話します。",
                ],
                practice: "Can I see the lease before I sign?",
            },
            zh: {
                heading: "签约前要确认的事",
                points: [
                    "不要只看房租。还要确认押金、水电费、停车、洗衣、宠物和提前搬走的规则。如果英文难，签字前可以要求时间阅读。",
                    "在美国，书面记录很重要。问题、维修请求和付款证明最好用邮件、短信或照片保存。",
                    "如果和室友同住，要早点说清楚打扫、安静时间、客人和公共用品的规则。",
                ],
                practice: "Can I see the lease before I sign?",
            },
        },
        utilities: {
            ja: {
                heading: "家の問題は早く、具体的に伝える",
                points: [
                    "水漏れ、暖房、電気、虫、鍵の問題は早めに連絡します。場所、問題、いつ始まったかを短く言えると対応が早くなります。",
                    "修理の人が来る時間は、午前9時から午後1時のように幅があることがあります。予定を空けておきましょう。",
                    "ゴミ、リサイクル、大型ゴミのルールは地域や建物で違います。近所や管理人に聞くのが普通です。",
                ],
                practice: "There is a leak under the sink.",
            },
            zh: {
                heading: "家里出问题要早说、说具体",
                points: [
                    "漏水、暖气、电、虫子、钥匙问题要尽早联系。能说清地点、问题和开始时间，处理会更快。",
                    "维修人员上门常常给一个时间段，比如上午9点到下午1点。那段时间要留在家或安排人开门。",
                    "垃圾、回收和大件垃圾规则每个城市或公寓不同。问邻居或管理员很正常。",
                ],
                practice: "There is a leak under the sink.",
            },
        },
        money: {
            ja: {
                heading: "お金の安全を守る",
                points: [
                    "銀行口座、デビットカード、クレジットカードは便利ですが、手数料を確認しましょう。特に毎月の手数料、ATM手数料、残高不足の手数料です。",
                    "電話やメッセージで、ギフトカード、暗号資産、送金アプリで急に払えと言われたら詐欺を疑います。",
                    "家賃、保証金、大きな買い物は必ずレシートや確認メールを残してください。",
                ],
                practice: "Are there any monthly fees?",
            },
            zh: {
                heading: "保护自己的钱",
                points: [
                    "银行账户、借记卡和信用卡很方便，但要确认费用，特别是月费、ATM费和透支费。",
                    "如果有人打电话或发信息，让你马上用礼品卡、加密货币或转账软件付款，要警惕诈骗。",
                    "房租、押金和大额购物一定要保存收据或确认邮件。",
                ],
                practice: "Are there any monthly fees?",
            },
        },
        shopping: {
            ja: {
                heading: "買い物では質問してよい",
                points: [
                    "店員に場所を聞くことは自然です。Excuse me で始めると丁寧に聞こえます。",
                    "表示価格に消費税が含まれていないことが多いので、レジで少し高くなることがあります。",
                    "返品にはレシート、未使用の状態、期限が必要なことがあります。店ごとにルールが違います。",
                ],
                practice: "Where can I find laundry detergent?",
            },
            zh: {
                heading: "买东西时可以开口问",
                points: [
                    "向店员问东西在哪里很自然。用 Excuse me 开头会更礼貌。",
                    "标价通常不包括销售税，所以结账时总价可能会高一点。",
                    "退货可能需要收据、未使用状态和期限。每家店规则不同。",
                ],
                practice: "Where can I find laundry detergent?",
            },
        },
        food: {
            ja: {
                heading: "食べ物ははっきり伝える",
                points: [
                    "アレルギーは遠慮せずに最初に言います。命に関わることがあるので、簡単な英語で強く伝えて大丈夫です。",
                    "レストランでは、残り物を持ち帰ることは普通です。box と言えば持ち帰り用の容器を頼めます。",
                    "着席式のレストランではチップを払う文化があります。地域や店で期待が違うので、レシートを確認しましょう。",
                ],
                practice: "I have a nut allergy.",
            },
            zh: {
                heading: "食物需求要说清楚",
                points: [
                    "过敏一定要一开始就说。因为可能有危险，用简单英文明确表达是可以的。",
                    "在餐厅把剩菜带回家很正常。说 box 就可以要打包盒。",
                    "坐下点餐的餐厅通常有给小费的习惯。不同地区和餐厅期待不同，可以看收据上的提示。",
                ],
                practice: "I have a nut allergy.",
            },
        },
        transportation: {
            ja: {
                heading: "移動前に方向と時間を確認",
                points: [
                    "バスや電車では、路線番号だけでなく方向も確認します。同じ番号でも逆方向に行くことがあります。",
                    "車を運転する場合、免許、保険、登録のルールは州ごとに違います。住む州のDMV情報を確認しましょう。",
                    "夜の移動、乗り換え、最終バスの時間を前もって調べると安全です。",
                ],
                practice: "Does this bus go to City College?",
            },
            zh: {
                heading: "出门前确认方向和时间",
                points: [
                    "坐公交或火车时，不只看线路号码，也要看方向。同一条线路可能去相反方向。",
                    "如果开车，驾照、保险和车辆登记规则按州不同。要查看所在州DMV的信息。",
                    "晚上出门、换乘和末班车时间最好提前查好，会更安全。",
                ],
                practice: "Does this bus go to City College?",
            },
        },
        health: {
            ja: {
                heading: "医療では正確さが一番大切",
                points: [
                    "緊急で命に関わる時は911です。最初に住所を言えるように練習しましょう。",
                    "軽い病気やけがは、かかりつけ医、クリニック、urgent care の方がERより合う場合があります。",
                    "症状、薬、アレルギー、保険をメモして持って行くと安心です。医療英語が難しい時は通訳を頼みましょう。",
                ],
                practice: "I need an interpreter, please.",
            },
            zh: {
                heading: "看病时准确最重要",
                points: [
                    "有生命危险的紧急情况拨打911。要练习先说出自己的地址。",
                    "轻微疾病或受伤，有时家庭医生、诊所或 urgent care 比急诊室更合适。",
                    "把症状、药物、过敏和保险信息写下来带去。医学英文困难时，可以要求口译。",
                ],
                practice: "I need an interpreter, please.",
            },
        },
        appointments: {
            ja: {
                heading: "時間と予約を守る文化",
                points: [
                    "アメリカでは予約時間を守ることが信頼につながります。初めての場所には早めに行くと安心です。",
                    "行けない時は、無断で行かないのではなく、早めにキャンセルまたは変更します。",
                    "日付は月/日/年で書かれることが多いです。06/07 は6月7日の意味になることが多いので注意しましょう。",
                ],
                practice: "I need to reschedule my appointment.",
            },
            zh: {
                heading: "重视时间和预约",
                points: [
                    "在美国，准时参加预约会让别人觉得你可靠。第一次去一个地方，最好提前到。",
                    "如果不能去，不要直接不出现，要尽早取消或改时间。",
                    "日期常写成月/日/年。比如06/07通常是6月7日，要特别注意。",
                ],
                practice: "I need to reschedule my appointment.",
            },
        },
        school: {
            ja: {
                heading: "学校とは早めに連絡する",
                points: [
                    "子どもが休む時は学校に連絡するのが普通です。理由を短く伝えれば大丈夫です。",
                    "学校からのメール、アプリ、プリントは大切です。遠足や医療、写真などは保護者の署名が必要なことがあります。",
                    "分からない時は、先生や事務室に説明や言語サポートを頼んでください。",
                ],
                practice: "My child was absent yesterday.",
            },
            zh: {
                heading: "要主动和学校联系",
                points: [
                    "孩子缺席时，通常需要通知学校。简单说明原因就可以。",
                    "学校邮件、App消息和纸质通知都很重要。郊游、医疗或拍照等活动可能需要家长签字。",
                    "不懂时，可以请老师或办公室解释，也可以要求语言帮助。",
                ],
                practice: "My child was absent yesterday.",
            },
        },
        work: {
            ja: {
                heading: "職場では確認が力になる",
                points: [
                    "勤務時間、休憩、給料日、制服、遅刻連絡の方法は最初に確認します。",
                    "分からない仕事は、黙って間違えるより、短く確認する方がよいです。Just to make sure... は便利です。",
                    "働く資格、税金、残業、福利厚生は状況で違います。重要な点は雇用主や専門家に確認しましょう。",
                ],
                practice: "Just to make sure, you want me to clock in here?",
            },
            zh: {
                heading: "工作中确认很重要",
                points: [
                    "一开始要确认班表、休息时间、发薪日、制服和迟到时怎么联系。",
                    "不懂任务时，简短确认比默默做错更好。Just to make sure... 很有用。",
                    "工作许可、税、加班和福利会因个人情况不同。重要问题要向雇主或专业人士确认。",
                ],
                practice: "Just to make sure, you want me to clock in here?",
            },
        },
        phone: {
            ja: {
                heading: "連絡手段を早く整える",
                points: [
                    "アメリカでは電話、留守番電話、SMS、メールをよく使います。留守番電話を聞く習慣をつけましょう。",
                    "契約ありのプランと契約なしのプランがあります。月額、データ量、解約料を確認します。",
                    "認証コードやパスワードを電話やメッセージで他人に教えないでください。",
                ],
                practice: "Can you text me the address?",
            },
            zh: {
                heading: "尽快建立联系方式",
                points: [
                    "在美国，电话、语音留言、短信和邮件都常用。要养成听语音留言的习惯。",
                    "手机套餐有合约和无合约。要确认月费、流量和取消费用。",
                    "不要通过电话或信息把验证码、密码告诉别人。",
                ],
                practice: "Can you text me the address?",
            },
        },
        mail: {
            ja: {
                heading: "住所は細かく正確に",
                points: [
                    "アパート番号、部屋番号、ZIPコードが抜けると郵便物が届かないことがあります。住所は一行ずつ正確に書きます。",
                    "USPSの転送は便利ですが、銀行、学校、医者、雇用主、政府機関には自分で住所変更を連絡します。",
                    "荷物はtracking numberで確認します。届かない時は、配送会社、建物の管理人、差出人に確認しましょう。",
                ],
                practice: "Please include my apartment number.",
            },
            zh: {
                heading: "地址要写完整、准确",
                points: [
                    "如果缺少公寓号、房间号或邮编，信件可能收不到。地址要一行一行写准确。",
                    "USPS转寄很方便，但银行、学校、医生、雇主和政府机构需要你自己通知新地址。",
                    "包裹可以用 tracking number 查询。没收到时，联系快递公司、楼管或寄件人。",
                ],
                practice: "Please include my apartment number.",
            },
        },
        safety: {
            ja: {
                heading: "緊急と非緊急を分ける",
                points: [
                    "火事、重大なけが、命の危険、犯罪が進行中なら911です。住所、何が起きたか、自分の名前を言います。",
                    "騒音、軽いトラブル、なくした物などは、地域の非緊急番号、管理人、市役所などが合う場合があります。",
                    "災害に備えて、水、薬、充電器、懐中電灯、重要書類のコピーを用意しておくと安心です。",
                ],
                practice: "What is your emergency?",
            },
            zh: {
                heading: "分清紧急和非紧急",
                points: [
                    "火灾、严重受伤、生命危险或正在发生的犯罪，要拨打911。先说地址，再说发生了什么和你的名字。",
                    "噪音、轻微问题或丢东西，可能更适合联系非紧急电话、楼管或市政府服务。",
                    "为灾害准备水、药、充电器、手电筒和重要文件复印件，会更安心。",
                ],
                practice: "What is your emergency?",
            },
        },
        community: {
            ja: {
                heading: "小さな会話が助けになる",
                points: [
                    "近所の人との短い挨拶は大切です。深い関係を作らなくても、困った時に質問しやすくなります。",
                    "How are you? は長い答えを求めていないことが多いです。Good, thanks. How about you? で十分です。",
                    "図書館やコミュニティセンターは、英語、パソコン、書類、地域情報の助けになることがあります。",
                ],
                practice: "Nice to meet you. I just moved in.",
            },
            zh: {
                heading: "小对话也能带来帮助",
                points: [
                    "和邻居简单打招呼很有用。即使不是很亲近，以后遇到问题也更容易开口问。",
                    "How are you? 很多时候只是问候，不一定需要长回答。Good, thanks. How about you? 就够了。",
                    "图书馆和社区中心可能提供英语、电脑、表格和本地信息方面的帮助。",
                ],
                practice: "Nice to meet you. I just moved in.",
            },
        },
        laundry: {
            ja: {
                heading: "共有の洗濯では時間とマナーが大切",
                points: [
                    "ランドリーでは、機械が止まったら早めに服を取り出します。他の人が待っていることがあります。",
                    "支払い方法は場所によって違います。硬貨、カード、アプリ、専用ランドリーカードなどがあります。",
                    "乾燥機では lint trap を確認します。ほこりを取ると乾きやすくなり、火事の危険も下がります。",
                ],
                practice: "Do I need quarters or a laundry card?",
            },
            zh: {
                heading: "共用洗衣要注意时间和礼貌",
                points: [
                    "在自助洗衣店或公寓洗衣房，机器停了以后要尽快取出衣服，因为别人可能在等。",
                    "付款方式每个地方不同，可能用硬币、银行卡、App或专用洗衣卡。",
                    "使用烘干机时要注意 lint trap。清理绒毛会让衣服更容易干，也能降低火灾风险。",
                ],
                practice: "Do I need quarters or a laundry card?",
            },
        },
        dryCleaning: {
            ja: {
                heading: "服を預ける前に値段と日付を確認",
                points: [
                    "ドライクリーニングでは、汚れ、取れたボタン、直してほしい場所を指で示すと伝わりやすいです。",
                    "pickup ticket は受け取りに必要です。紙、メール、SMSのどれでも、なくさないようにしましょう。",
                    "しみ抜きや直しは必ず成功するとは限りません。料金、仕上がり日、できることを先に確認します。",
                ],
                practice: "I am here to pick up my order.",
            },
            zh: {
                heading: "把衣服留下前先确认价格和日期",
                points: [
                    "去干洗店时，用手指出污渍、掉扣子或需要修改的地方，会更容易说明。",
                    "pickup ticket 是取衣服时的重要凭证。纸条、邮件或短信都要保存好。",
                    "去污或修改不一定百分之百成功。离开前先确认费用、完成日期和可以做到什么。",
                ],
                practice: "I am here to pick up my order.",
            },
        },
        taxis: {
            ja: {
                heading: "乗る前に車と行き先を確認",
                points: [
                    "配車アプリでは、乗る前に運転手の名前、車種、ナンバープレートを確認します。",
                    "空港ではタクシーや配車の乗り場が決まっていることがあります。案内表示に従いましょう。",
                    "知らない人から空港内で直接ライドを勧められたら注意します。公式のタクシー乗り場やアプリを使う方が安全です。",
                ],
                practice: "Are you my driver?",
            },
            zh: {
                heading: "上车前确认车和目的地",
                points: [
                    "使用网约车App时，上车前要确认司机姓名、车型和车牌号。",
                    "机场的出租车或网约车通常有指定上车区，不一定在行李提取处门口。",
                    "如果陌生人在机场里面主动拉客，要小心。使用正式出租车区或App更安全。",
                ],
                practice: "Are you my driver?",
            },
        },
        carCare: {
            ja: {
                heading: "車では表示を読む力が必要",
                points: [
                    "駐車標識は時間、曜日、場所によって変わります。短い文でも、No parking や permit only は必ず確認しましょう。",
                    "ガソリンスタンドではカードで払う時にZIPコードを求められることがあります。うまくいかない時は店内で払えます。",
                    "車のトラブルでは、まず安全な場所に移動します。その後、保険会社、ロードサービス、修理店に連絡します。",
                ],
                practice: "Is parking allowed here?",
            },
            zh: {
                heading: "开车生活需要会看标志",
                points: [
                    "停车标志会根据时间、日期和地点变化。即使英文短，也要注意 No parking 和 permit only。",
                    "加油站刷卡时，有时会要求输入ZIP code。如果机器不成功，可以进店付款。",
                    "车出问题时，先把车移到安全地方，然后联系保险、道路救援或修车店。",
                ],
                practice: "Is parking allowed here?",
            },
        },
        personalCare: {
            ja: {
                heading: "写真と短い表現が役に立つ",
                points: [
                    "ヘアカットでは、長さやスタイルを英語だけで説明するのは難しいことがあります。写真を見せると安全です。",
                    "walk-in は予約なしの客です。ただし待ち時間が長いこともあるので、時間が限られている時は予約しましょう。",
                    "髪、ネイル、美容サービスではチップを渡す人が多いです。最終料金を見てから判断して大丈夫です。",
                ],
                practice: "Just a trim, please.",
            },
            zh: {
                heading: "照片和短句很有帮助",
                points: [
                    "剪头发时，只用英文解释长度和发型可能很难。给对方看照片会更安全。",
                    "walk-in 指没有预约的客人。不过可能要等很久，所以时间紧时最好预约。",
                    "头发、美甲和美容服务通常有人给小费。可以看最后价格后再决定。",
                ],
                practice: "Just a trim, please.",
            },
        },
        clothingServices: {
            ja: {
                heading: "交換と修理は証拠が大切",
                points: [
                    "服の交換では、レシート、タグ、未使用の状態が必要なことが多いです。買った後すぐ捨てないようにしましょう。",
                    "tailor に頼む時は、実際に着て長さを確認することがあります。時間に余裕を持って行きます。",
                    "小さな修理でも料金が高いことがあります。先に Can I get an estimate? と聞くと安心です。",
                ],
                practice: "I need to exchange this for a larger size.",
            },
            zh: {
                heading: "换货和修理都需要凭证",
                points: [
                    "换衣服时，通常需要收据、吊牌和未使用状态。买完以后不要马上丢掉这些东西。",
                    "找裁缝修改时，可能需要你穿上衣服，让对方标记长度。最好留出时间。",
                    "小修理也可能不便宜。可以先问 Can I get an estimate?，意思是想知道大概价格。",
                ],
                practice: "I need to exchange this for a larger size.",
            },
        },
        recreation: {
            ja: {
                heading: "楽しい場所にも契約とルールがある",
                points: [
                    "ジムでは月額料金だけでなく、入会金、解約方法、契約期間を確認します。",
                    "公園や運動施設には、ペット、飲酒、火の使用、予約、閉園時間などのルールがあります。",
                    "共有スペースでは、自分が使った場所をきれいにして次の人に渡すことが期待されます。",
                ],
                practice: "Can I try one class first?",
            },
            zh: {
                heading: "休闲场所也有合同和规则",
                points: [
                    "加入健身房时，不只看月费，也要确认入会费、取消方法和合同期限。",
                    "公园和运动场可能有宠物、酒精、用火、预约和关闭时间等规则。",
                    "使用公共空间后，要把桌子、器材或房间整理好，方便下一个人使用。",
                ],
                practice: "Can I try one class first?",
            },
        },
        serviceProblems: {
            ja: {
                heading: "問題は落ち着いて、具体的に伝える",
                points: [
                    "困った時は、何が起きたか、いつ起きたか、今何をしてほしいかを短く伝えます。",
                    "case number、receipt、email、ticket number は後で確認するために大切です。必ずメモや写真で残しましょう。",
                    "最初の人が助けられない時は、怒らずに Who should I speak with? と聞くと次につながりやすいです。",
                ],
                practice: "Can I get a case number?",
            },
            zh: {
                heading: "遇到问题要冷静、具体地说明",
                points: [
                    "有问题时，简短说明发生了什么、什么时候发生、现在需要对方做什么。",
                    "case number、receipt、email 和 ticket number 对后续查询很重要，要保存或拍照。",
                    "如果第一个人不能帮忙，不要生气。问 Who should I speak with? 会更容易找到负责的人。",
                ],
                practice: "Can I get a case number?",
            },
        },
    };

    function getStoredLanguage() {
        try {
            return window.localStorage.getItem(STORAGE_KEY);
        } catch (error) {
            return null;
        }
    }

    function storeLanguage(language) {
        try {
            window.localStorage.setItem(STORAGE_KEY, language);
        } catch (error) {
            // Local storage can be disabled; the selector still works for this page view.
        }
    }

    function createElement(tagName, className, textContent) {
        const element = document.createElement(tagName);
        if (className) {
            element.className = className;
        }
        if (textContent !== undefined) {
            element.textContent = textContent;
        }
        return element;
    }

    function renderExplanation(container, languageKey) {
        const moduleKey = container.dataset.explanation;
        const language = languages[languageKey] || languages.ja;
        const explanation = explanations[moduleKey]?.[languageKey] || explanations[moduleKey]?.ja;

        container.replaceChildren();
        container.setAttribute("lang", language.lang);

        if (!explanation) {
            container.append(createElement("p", "language-empty", "Explanation unavailable."));
            return;
        }

        const label = createElement("p", "language-label", `${language.headingPrefix}: ${language.label}`);
        const heading = createElement("h3", null, explanation.heading);
        const remember = createElement("strong", "language-subhead", language.rememberLabel);
        const list = createElement("ul", "language-points");

        explanation.points.forEach((point) => {
            list.append(createElement("li", null, point));
        });

        const practiceLabel = createElement("strong", "language-subhead", language.practiceLabel);
        const practice = createElement("p", "language-practice", explanation.practice);

        container.append(label, heading, remember, list, practiceLabel, practice);
    }

    function renderLanguage(languageKey) {
        document.querySelectorAll("[data-explanation]").forEach((container) => {
            renderExplanation(container, languageKey);
        });
    }

    function setupLanguageSelector() {
        const select = document.querySelector("#life-language-select");
        if (!select) {
            return;
        }

        const storedLanguage = getStoredLanguage();
        const initialLanguage = languages[storedLanguage] ? storedLanguage : "ja";
        select.value = initialLanguage;
        renderLanguage(initialLanguage);

        select.addEventListener("change", () => {
            const languageKey = languages[select.value] ? select.value : "ja";
            storeLanguage(languageKey);
            renderLanguage(languageKey);
        });
    }

    setupLanguageSelector();
})();
